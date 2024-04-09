from typing import AsyncIterable, Iterable
from pydantic import BaseModel
import haskellian.either as E
from moveread.core import ImageID, ops
from moveread.sdk import MovereadAPI
from moveread.boxes.annotations import RobustExtractionResult
from ..scripts.extract_ import ExtractMeta

class ExtractItem(BaseModel):
  imageId: ImageID
  contoured_url: str
  annotation: RobustExtractionResult | None = None

async def items(games: Iterable[str], api: MovereadAPI) -> AsyncIterable[ExtractItem]:
  for gameId in games:
    try:
      game = (await api.games.read(gameId)).unsafe()
      for imgId, image in ops.images(game):
        try:
          meta = E.validate(image.meta, ExtractMeta).unsafe()
          r = E.maybe(meta.robust_extract_result).unsafe().unsafe()
          url = f'blobs/{r.contoured_url}.jpg'
          yield ExtractItem(imageId=imgId, contoured_url=url, annotation=meta.robust_extraction)
        except E.IsLeft:
          ...
    except E.IsLeft as e:
      print(f'Error reading game {gameId}:', e)