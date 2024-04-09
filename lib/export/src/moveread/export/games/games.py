import asyncio
import haskellian.either as E
from moveread.core import Game, CoreAPI
from moveread.annotations.games import parse_pgn
from moveread.errors import MissingMeta, InvalidData
from .. import players

def export_labels(game: Game):
  return parse_pgn(game.meta).fmap(
    lambda pgn: [players.export_labels(player, pgn) for player in game.players]
  )

async def export_boxes(game: Game, *, api: CoreAPI):
  tasks = [players.export_boxes(player, api=api) for player in game.players]
  return await asyncio.gather(*tasks)

async def export_samples(game: Game, *, api: CoreAPI) -> E.Either[MissingMeta|InvalidData, list[players.SamplesResult]]:
  match parse_pgn(game.meta):
    case E.Right(pgn):
      return E.Right(await asyncio.gather(*[
        players.export_samples(player, pgn, api=api) for player in game.players
      ]))
    case err:
      return err # type: ignore