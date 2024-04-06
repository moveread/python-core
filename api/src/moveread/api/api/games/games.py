from typing import Annotated
from fastapi import APIRouter, Response, status, File
import haskellian.either as E
from moveread.core import Game
from moveread.sdk import MovereadAPI
from moveread.errors import DBError, InvalidData, InexistentItem

def router(sdk: MovereadAPI):
  app = APIRouter()

  @app.get('/')
  async def list_games(batch_size: int | None = None) -> list[E.Either[DBError, str]]:
    return await sdk.games.list(batch_size)
  
  @app.get('/{id}')
  async def read_game(id: str, response: Response) -> E.Either[DBError|InvalidData|InexistentItem, Game]:
    result = await sdk.games.read(id)
    if E.is_left(result):
      response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
    return result
  
  @app.post('/{id}', status_code=status.HTTP_201_CREATED)
  async def create_game(
    id: str, response: Response,
    white: Annotated[list[bytes], File(description="White's images")],
    black: Annotated[list[bytes], File(description="Black's images")] | None = None,
  ) -> E.Either[DBError, Game]:
    imgs = [white] if black is None else [white, black]
    result = await sdk.games.create(id, imgs)
    if E.is_left(result):
      response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
    return result
  
  @app.put('/{id}')
  async def upsert_game(id: str, game: Game, response: Response) -> E.Either[DBError, None]:
    result = await sdk.core.games.insert(id, game, replace=True)
    if E.is_left(result):
      response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
    return result 
  
  return app