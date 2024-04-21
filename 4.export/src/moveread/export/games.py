import asyncio
from typing import Sequence
from haskellian import Either, Left, Right, Iter
from moveread.core import Game, CoreAPI
from moveread.errors import MissingMeta
from .players import player_labels, player_boxes, player_samples, ChessError, Sample

def game_labels(game: Game) -> list[Either[ChessError|MissingMeta, list[str]]]:
  pgn = game.meta and game.meta.pgn
  if pgn is None:
    return [Left(MissingMeta('Game has no PGN annotation'))]
  return [player_labels(player, pgn) for player in game.players]

async def game_boxes(game: Game, *, api: CoreAPI):
  tasks = [player_boxes(player, api=api) for player in game.players]
  return await asyncio.gather(*tasks)

async def game_samples(game: Game, *, api: CoreAPI) -> Sequence[Either[ChessError|MissingMeta, Sample]]:
  pgn = game.meta and game.meta.pgn
  if pgn is None:
    return [Left(MissingMeta('Game has no PGN annotation'))]
  samples = await asyncio.gather(*[player_samples(player, pgn, api=api) for player in game.players])
  return Iter(samples).flatmap(lambda e: e.match(
    lambda err: [Left(err)],
    lambda ok: [Right(sample) for sample in ok]
  )).sync()