from typing import Literal
from dataclasses import dataclass
from pydantic import BaseModel
from kv.api import KV

Source = Literal['llobregat23', 'original-train', 'original-test', 'original-val']

class Dataset(BaseModel):
  file: str
  source: Source

@dataclass
class DatasetsAPI:
  meta: KV[Dataset]
  data: KV[bytes]

  @classmethod
  def at(cls, path: str) -> 'DatasetsAPI':
    import os
    from kv.sqlite import SQLiteKV
    from kv.fs import FilesystemKV
    return DatasetsAPI(
      meta=SQLiteKV.validated(Dataset, os.path.join(path, 'meta.sqlite'), table='datasets'),
      data=FilesystemKV[bytes](os.path.join(path, 'data'))
    )