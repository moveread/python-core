from typing import NamedTuple
import asyncio
from haskellian import Either, Left, IsLeft, Right, iter as I
from cv2 import Mat
from moveread.core import Player, CoreAPI
from moveread.labels import export, ChessError
from .sheets import sheet_boxes

async def player_boxes(player: Player, *, api: CoreAPI):
  boxes = await asyncio.gather(*[sheet_boxes(sheet, api=api) for sheet in player.sheets])
  return list(I.flatten(boxes))

def player_labels(player: Player, pgn: list[str]) -> Either[ChessError, list[str]]:
  return Right(pgn) if player.meta is None else export(pgn, player.meta)

class Sample(NamedTuple):
  box: Mat
  label: str

async def player_samples(player: Player, pgn: list[str], *, api: CoreAPI) -> Either[ChessError, list[Sample]]:
  try:
    labels = player_labels(player, pgn).unsafe()
    boxes = await player_boxes(player, api=api)
    return Right([
      Sample(b, lab)
      for bxs, lab in zip(boxes, labels)
        for b in bxs
    ])
  except IsLeft as e:
    return Left(e.value)