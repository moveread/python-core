from typing import Any
from pydantic import BaseModel, RootModel, ConfigDict, ValidationError
import haskellian.either as E
from moveread.errors import InvalidMeta, InvalidData, InexistentSchema, MissingMeta

class Tournament(BaseModel):
  model_config = ConfigDict(extra='allow')
  name: str | None = None
  group: str | None = None
  round: int | None = None
  board: int | None = None

class Headers(BaseModel):
  model_config = ConfigDict(extra='allow')
  event: str | None = None
  site: str | None = None
  date: str | None = None
  round: int | None = None
  white: str | None = None
  black: str | None = None
  result: str | None = None

class GameMeta(BaseModel):
  model_config = ConfigDict(extra='allow')
  tournament: Tournament | None = None
  headers: Headers | None = None
  pgn: str | None = None

def parse_pgn(meta: dict | None) -> E.Either[MissingMeta|InvalidData, list[str]]:
  if not meta or not 'pgn' in meta:
    return E.Left(MissingMeta('No PGN annotation'))
  elif not isinstance(meta['pgn'], str):
    return E.Left(InvalidData(f'Expected PGN to be `str`, but is {type(meta["pgn"])}'))
  else:
    return E.Right(meta['pgn'].split(' '))
