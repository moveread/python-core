from typing import Literal
import haskellian.asyn as hka
import haskellian.either as E
from fastapi import FastAPI, Response
from fastapi.routing import APIRouter
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from moveread.core import ImageID
from moveread.sdk import MovereadAPI
from .ops import items, ExtractItem, RobustExtractionResult, ExtractMeta

def router(api: MovereadAPI, games: list[str] | None = None):

  router = APIRouter()

  @router.get('/items')
  async def get_items() -> list[ExtractItem]:
    gameIds = games or E.filter(await api.games.list())
    return await hka.syncify(items(gameIds, api))
  
  @router.post('/annotate')
  async def annotate(imageId: ImageID, annotation: RobustExtractionResult | Literal['null'], response: Response):
    ann = None if annotation == 'null' else annotation
    result = await api.images.annotate(imageId, ExtractMeta(robust_extraction=ann))
    if result.tag == 'left':
      response.status_code = 500
    return result

  return router


def make_app(api: MovereadAPI, *, games: list[str] | None = None, blobs_path: str | None = None):
  app = FastAPI(generate_unique_id_function=lambda route: route.name)
  app.include_router(router(api, games))
  app.add_middleware(
      CORSMiddleware,
      allow_origins=["*"],
      allow_credentials=True,
      allow_methods=["*"],
      allow_headers=["*"],
  )
  if blobs_path is not None:
    app.mount('/blobs', StaticFiles(directory=blobs_path), name='blobs')
  return app