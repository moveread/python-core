from dataclasses import dataclass
import os
import sqlite3
import haskellian.either as E
from kv.sqlite import SQLiteKV
from kv.fs import FilesystemKV
from kv.api import KV
from kv.api.errors import InvalidData
from moveread.core import CoreAPI, Game

def parse_game(x: str | bytes) -> E.Either[InvalidData, Game]:
  return E.validate_json(x, Game).mapl(lambda e: InvalidData(str(e)))

@dataclass
class LocalAPI(CoreAPI):
  
  @classmethod
  def at(cls, base_path: str, blobs_extension: str = '.jpg') -> 'LocalAPI':
    os.makedirs(base_path, exist_ok=True)
    db_path = os.path.join(base_path, 'games.sqlite')
    conn = sqlite3.connect(db_path)
    blobs_path = os.path.join(base_path, 'blobs')
    os.makedirs(blobs_path, exist_ok=True)
    return cls(conn=conn, blobs_path=blobs_path, blobs_extension=blobs_extension)

  conn: sqlite3.Connection
  blobs_path: str = 'blobs'
  blobs_extension: str = '.jpg'

  def __post_init__(self):
    self._blobs: KV[bytes] = FilesystemKV[bytes](base_path=self.blobs_path, extension=self.blobs_extension)
    self._games: KV[Game] = SQLiteKV[Game](
      conn=self.conn, table='games', dtype='JSON',
      parse=parse_game,
      dump=lambda game: game.model_dump_json(exclude_none=True)
    )

  @property
  def blobs(self) -> KV[bytes]:
    return self._blobs
  @property
  def games(self) -> KV[Game]:
    return self._games