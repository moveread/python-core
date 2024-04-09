from typing import NamedTuple, Iterable
import asyncio
import haskellian.either as E
from haskellian.iterables import transpose
from cv2 import Mat
from moveread.core import Player, CoreAPI
from moveread.errors import InvalidData, DBError, InexistentItem, MissingMeta
from ..sheets import boxes, BoxesResult as SheetBoxesResult, BoxesErr

class BoxesResult(NamedTuple):
  boxes: list[tuple[Mat, ...]]
  """Ply-major boxes (may have multiple boxes per ply if a sheet has multiple image versions)"""
  errors: list

def format_errors(results: list[SheetBoxesResult]) -> list:
  return [
    r.match(lambda e: e, lambda x: list(E.filter_lefts(x)))
    for r in results
  ]

def format_boxes(results: list[SheetBoxesResult]) -> list[tuple[Mat, ...]]:
  res: list[tuple[Mat, ...]] = []
  for sheet_res in E.take_while(results):
    res.extend(transpose(E.filter(sheet_res)))
  return res

async def export_boxes(
  player: Player, *, api: CoreAPI
) -> BoxesResult:
  results = await asyncio.gather(*[boxes(sheet, api=api) for sheet in player.sheets])
  return BoxesResult(format_boxes(results), format_errors(results))