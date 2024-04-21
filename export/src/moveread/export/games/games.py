import asyncio
import haskellian.either as E
from moveread.core import Game, CoreAPI
from moveread.annotations.games import GameMeta
from moveread.errors import MissingMeta, InvalidData
from .. import players

def export_labels(game: Game):
  return E.validate(game.meta, GameMeta).fmap(
    lambda meta: [players.export_labels(player, meta.pgn) for player in game.players]
  )

async def export_boxes(game: Game, *, api: CoreAPI):
  tasks = [players.export_boxes(player, api=api) for player in game.players]
  return await asyncio.gather(*tasks)

async def export_samples(game: Game, *, api: CoreAPI) -> E.Either[MissingMeta|InvalidData, list[players.SamplesResult]]:
  match E.validate(game.meta, GameMeta):
    case E.Right(meta):
      return E.Right(await asyncio.gather(*[
        players.export_samples(player, pgn=meta.pgn, api=api) for player in game.players
      ]))
    case err:
      return err # type: ignore