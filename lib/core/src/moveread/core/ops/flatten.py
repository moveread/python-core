from typing import Iterable
from ..models import Game, Player, Sheet, Image, PlayerID, SheetID, ImageID

def players(game: Game) -> Iterable[tuple[PlayerID, Player]]:
  for i, player in enumerate(game.players):
    yield PlayerID(game.id, i), player

def sheets(game: Game) -> Iterable[tuple[SheetID, Sheet]]:
  for i, player in enumerate(game.players):
    for j, sheet in enumerate(player.sheets):
      yield SheetID(game.id, i, j), sheet

def images(game: Game) -> Iterable[tuple[ImageID, Image]]:
  for sheetId, sheet in sheets(game):
    for version, image in enumerate(sheet.images):
      yield sheetId.imageId(version), image