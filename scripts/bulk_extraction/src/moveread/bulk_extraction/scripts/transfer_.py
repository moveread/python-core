import haskellian.either as E
from moveread.sdk import MovereadAPI
from moveread.core import ops
from ramda import omit
from .extract_.types import ExtractMeta

async def transfer(games: list[str], output: MovereadAPI, result: MovereadAPI):
  """Merge extracted `games` from `output` (generated via the `extract` script) into `result`
  - If correct, adds to images meta `'box_contours'`, `'source'` and `'robust_result'`, whilst preserving any other metadata
  """
  for gameId in games:
    game = (await output.games.read(gameId)).unsafe()
    for imgId, image in ops.images(game):
      print(f'\r{imgId}', end='', flush=True)
      try:
        meta = E.validate(image.meta, ExtractMeta).unsafe()
        match meta.robust_extraction:
          case 'failed' | 'incorrect':
            continue
          case 'perspective-correct' |'correct' as robust_result:
            # move corrected image
            res = E.maybe(meta.robust_extract_result).unsafe().unsafe()
            corr_img = (await output.core.blobs.read(res.corrected_url)).unsafe()
            old_meta: dict = omit(['robust_extract_result'], meta.model_dump(exclude_none=True)) # type: ignore
            new_meta = old_meta | ExtractMeta(
              source='robust-corrected', robust_extraction=robust_result,
              box_contours=res.contours if robust_result == 'correct' else None
            ).model_dump(exclude_none=True)
            (await result.images.upsert(imgId, corr_img, new_meta)).unsafe()
      except E.IsLeft as e:
        print(f'Error transfering {imgId}:', e, flush=True)
        