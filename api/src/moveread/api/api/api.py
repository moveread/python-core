from fastapi import FastAPI
from moveread.sdk import MovereadAPI
from . import games, images

def app(sdk: MovereadAPI):
  app = FastAPI()
  app.include_router(games.router(sdk), tags=['games'], prefix='/games')
  app.include_router(images.router(sdk), tags=['images'], prefix='/images')

  @app.get('/')
  def ping():
    return 'Pong'

  return app
