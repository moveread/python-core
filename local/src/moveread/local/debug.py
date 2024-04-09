from dataclasses import dataclass
import os
import sqlite3
from pydantic import ValidationError
import haskellian.either as E
from kv.sqlite import SQLiteKV
from kv.fs import FilesystemKV
from kv.api import AsyncAPI
from kv.api.asyncify import Asyncify
from kv.api.errors import InvalidData
from moveread.core import CoreAPI, Game

def parse_game(x: str | bytes) -> E.Either[InvalidData, Game]:
  return E.validate_json(x, Game).mapl(lambda e: InvalidData(str(e)))

@dataclass
class DebugAPI(CoreAPI):
  
  @classmethod
  def at(cls, base_path: str, blobs_extension: str = '.jpg') -> 'DebugAPI':
    os.makedirs(base_path, exist_ok=True)
    json_path = os.path.join(base_path, 'games')
    blobs_path = os.path.join(base_path, 'blobs')
    os.makedirs(json_path, exist_ok=True)
    os.makedirs(blobs_path, exist_ok=True)
    return cls(json_path=json_path, blobs_path=blobs_path, blobs_extension=blobs_extension)

  json_path: str = 'games'
  blobs_path: str = 'blobs'
  blobs_extension: str = '.jpg'

  def __post_init__(self):
    self._blobs: AsyncAPI[bytes] = Asyncify(FilesystemKV[bytes](base_path=self.blobs_path, extension=self.blobs_extension))
    self._games: AsyncAPI[Game] = Asyncify(FilesystemKV[Game](
      base_path=self.json_path, extension='.json',
      parse=parse_game,
      dump=lambda game: game.model_dump_json(exclude_none=True)
    ))

  @property
  def blobs(self) -> AsyncAPI[bytes]:
    return self._blobs
  @property
  def games(self) -> AsyncAPI[Game]:
    return self._games