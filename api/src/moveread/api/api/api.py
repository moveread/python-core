from fastapi import FastAPI
from fastapi.routing import APIRoute
from fastapi.middleware.cors import CORSMiddleware
from moveread.sdk import MovereadAPI
from . import games, images


def make_app(sdk: MovereadAPI):
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

  @app.get('/')
  def ping():
    return 'Pong'

  return app
