from typing import Annotated
from fastapi import FastAPI, File
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from moveread.sdk import MovereadAPI
from . import games, images, ops


def make_app(sdk: MovereadAPI, blobs_path: str | None = None):
  app = FastAPI(generate_unique_id_function=lambda route: route.name)
  app.add_middleware(
      CORSMiddleware,
      allow_origins=["*"],
      allow_credentials=True,
      allow_methods=["*"],
      allow_headers=["*"],
  )
  app.include_router(games.router(sdk), tags=['games'], prefix='/games')
  app.include_router(images.router(sdk), tags=['images'], prefix='/images')
  app.include_router(ops.router, tags=['ops'])

  if blobs_path is not None:
    app.mount('/blobs', StaticFiles(directory=blobs_path), name='blobs')

  @app.get('/')
  def ping():
    return 'Pong'

  # @app.get('/blob')
  # async def read_blob(id: str):
  #   return sdk.core.blobs.read(id)

  return app
