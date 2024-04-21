import os
from moveread.core import CoreAPI, Game
from kv.sqlite import SQLiteKV
from kv.fs import FilesystemKV

def LocalAPI(path: str) -> CoreAPI:
  return CoreAPI(
    games=SQLiteKV.validated(Game, os.path.join(path, 'games.sqlite'), table='games'),
    blobs=FilesystemKV[bytes](os.path.join(path, 'blobs'))
  )

def DebugAPI(path: str) -> CoreAPI:
  return CoreAPI(
    games=FilesystemKV.validated(Game, os.path.join(path, 'games')),
    blobs=FilesystemKV[bytes](os.path.join(path, 'blobs'))
  )