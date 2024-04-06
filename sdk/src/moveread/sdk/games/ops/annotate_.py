import haskellian.either as E
from moveread.core import CoreAPI, Game
from moveread.annotations.games import validate
from moveread.errors import InvalidMeta, DBError, InvalidData, InexistentItem, InexistentGame

async def annotate(gameId: str, schema: str, metadata: dict, *, api: CoreAPI) -> E.Either[InvalidMeta|InexistentGame|InvalidData|DBError, Game]:
   try:
      meta = validate(schema, metadata).unsafe()
      game = (await api.games.read(gameId)).unsafe()
      game.meta = (game.meta or {}) | dict(schema=meta)
      (await api.games.update(gameId, game)).unsafe()
      return E.Right(game)
   except E.IsLeft as e:
      if isinstance(e.value, InexistentItem):
         return E.Left(InexistentGame(gameId, e.value))
      return E.Left(e.value)