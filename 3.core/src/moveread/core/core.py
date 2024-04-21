from typing import TypeVar, Any
from dataclasses import dataclass
import asyncio
import haskellian.either as E
from kv.api import KV
from .models import Game

T = TypeVar('T')

@dataclass
class CoreAPI:

  games: KV[Game]
  blobs: KV[bytes]

  @classmethod
  def at(cls, path: str) -> 'CoreAPI':
    from .local import LocalAPI
    return LocalAPI(path)
  
  @classmethod
  def debug(cls, path: str) -> 'CoreAPI':
    from .local import DebugAPI
    return DebugAPI(path)

  async def rollback(self) -> E.Either[Any, None]:
    eithers = await asyncio.gather(
      self.games.rollback(),
      self.blobs.rollback()
    )
    return E.sequence(eithers) | (lambda _: None)
  
  async def commit(self) -> E.Either[Any, None]:
    eithers = await asyncio.gather(
      self.games.commit(),
      self.blobs.commit()
    )
    return E.sequence(eithers) | (lambda _: None)
  