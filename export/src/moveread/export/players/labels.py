import haskellian.either as E
from moveread.core import Player
from moveread.errors import InvalidData
from moveread.annotations.players import PlayerMeta
from moveread.labels import export, ChessError

def export_labels(player: Player, pgn: list[str]) -> E.Either[InvalidData|ChessError, list[str]]:
  return E.validate(player.meta or {}, PlayerMeta).mapl(
    lambda e: InvalidData(str(e))
  ).bind(
    lambda ann: export(pgn, ann)
  )
