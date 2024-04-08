from typing import Annotated
from fastapi import APIRouter, Response, status, File
import haskellian.either as E
from moveread.core import Game, SheetID, ImageID
from moveread.sdk import MovereadAPI
from moveread.errors import DBError, InvalidData, InexistentGame, InexistentSheet, InexistentPlayer, InexistentImage, InvalidMeta

def router(sdk: MovereadAPI):
  app = APIRouter()

  @app.post('/', name='Add/modify Image')
  async def upsert_image(
    gameId: str, player: int, page: int, *, version: int | None = None,
    img: Annotated[bytes, File()], response: Response
  ) -> E.Either[InexistentGame|InexistentSheet|InexistentPlayer|InexistentImage|InvalidData|DBError, Game]:
    id = SheetID(gameId, player, page)
    result = await sdk.images.upsert(id, img, version=version)
    if E.is_left(result):
      if result.value.reason == 'db-error' or result.value.reason == 'invalid-data':
        response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
      else:
        response.status_code = status.HTTP_400_BAD_REQUEST
    return result
  
  @app.put('/annotate')
  async def annotate_image(
    gameId: str, player: int, page: int, version: int,
    schema: str, meta: str | list | dict, response: Response
  ) -> E.Either[InvalidMeta|InvalidData|InexistentGame|InexistentPlayer|InexistentSheet|InexistentImage|DBError, Game]:
    result = await sdk.images.annotate(ImageID(gameId, player, page, version), schema, meta)
    if E.is_left(result):
      response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
    return result

  return app