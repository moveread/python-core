from typing import Any, AsyncIterable
from functools import partial
import asyncio
from uuid import uuid4
import haskellian.either as E
import haskellian.asyn as hka
from moveread.core import Game, CoreAPI, ImageID, ops
from moveread.sdk import MovereadAPI
import pure_cv as vc
import robust_extraction as re
import robust_extraction.templates as ts
from .types import ExtractMeta, Result, ExtractTask

async def store_result(res: re.Result, output: MovereadAPI, contoured_height = 512) -> E.Either[Any, Result]:
  corr = vc.encode(res.corr_img, '.jpg') # type: ignore
  cont = vc.draw.contours(res.contours, res.corr_img) # type: ignore
  cont = vc.descale_h(cont, contoured_height)
  cont = vc.encode(cont, '.jpg')
  corr_id = f'corrected/{uuid4()}'
  cont_id = f'contoured/{uuid4()}'
  results = E.sequence(await asyncio.gather(
    output.core.blobs.insert(corr_id, corr),
    output.core.blobs.insert(cont_id, cont),
  ))
  if E.is_left(results):
    return E.Left(f'Error saving contoured/corrected images: {results}')

  return E.Right(Result(contours=res.contours.tolist(), corrected_url=corr_id, contoured_url=cont_id))

async def postprocess(imageId: ImageID, res: E.Either[Any, re.Result], output: MovereadAPI):
  result = await store_result(res.value, output) if E.is_right(res) else res
  meta = ExtractMeta(robust_extract_result=result) # type: ignore
  return await output.images.annotate(imageId, meta)

async def tasks(game: Game, api: CoreAPI, *, modelId: ts.ModelID) -> AsyncIterable[ExtractTask]:
  try:
    for sid, sheet in ops.sheets(game):
      version = len(sheet.images) - 1
      image = E.safe(lambda: sheet.images[version]).unsafe()
      img = (await api.blobs.read(image.url)).unsafe()
      yield ExtractTask(img=img, imageId=sid.imageId(version), modelId=modelId)
  except E.IsLeft as e:
    print(f'Error generating tasks for {game.id}:', e)

def safe_extract(task: ExtractTask) -> E.Either[Any, re.Result]:
  mat = vc.decode(task.img)
  try:
    return re.descaled_extract(mat, ts.models[task.modelId], descale_h=1496)
  except Exception as e:
    return E.Left(str(e))

async def run_task(task: ExtractTask, output: MovereadAPI):
  res = safe_extract(task)
  return await postprocess(task.imageId, res, output)

async def all_tasks(games: list[str], input: MovereadAPI, output: MovereadAPI, *, modelId: ts.ModelID):
  for i, gameId in enumerate(games):
    try:
      game = (await input.core.games.read(gameId)).unsafe()
      (await output.core.games.insert(game.id, game)).unsafe()
      async for t in tasks(game, input.core, modelId=modelId):
        print(f'\r[{i} / {len(games)}]: {t.imageId}', end=' ', flush=True)
        yield t
    except E.IsLeft as e:
      print(f'Error with IO of {gameId}:', e)

async def run(games: list[str], input: MovereadAPI, output: MovereadAPI, *, modelId: ts.ModelID):
  """Extract `games` (read from `input`) into `output`"""
  tasks = all_tasks(games, input, output, modelId=modelId)
  outputs = hka.concurrent_map(partial(run_task, output=output), tasks)
  async for x in outputs:
    yield x
