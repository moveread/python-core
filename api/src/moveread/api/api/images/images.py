from typing import Annotated
from fastapi import APIRouter, Response, status, File
import haskellian.either as E
from moveread.core import Game, SheetID
from moveread.sdk import MovereadAPI
from moveread.errors import DBError, InvalidData, InexistentGame, InexistentSheet, InexistentPlayer

def router(sdk: MovereadAPI):
  app = APIRouter()

  @app.post('/{gameId}/{player}/{page}', name='Add Image')
  @app.put('/{gameId}/{player}/{page}/{version}', name='Modify image')
  async def upsert_image(
    gameId: str, player: int, page: int, *, version: int | None = None,
    img: Annotated[bytes, File()], response: Response
  ) -> E.Either[InexistentGame|InexistentSheet|InexistentPlayer|InvalidData|DBError, Game]:
    id = SheetID(gameId, player, page)
    result = await sdk.images.upsert(id, img, version=version)
    if E.is_left(result):
      response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
    return result
  
  return app