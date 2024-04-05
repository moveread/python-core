from haskellian.either import Either, Left, Right
import chess
from chess import IllegalMoveError, InvalidMoveError, AmbiguousMoveError
from chess_notation.styles import Styles, style
from chess_notation.language import translate
from chess_utils import captured_piece
from ..annotations import Annotations

ChessError = IllegalMoveError | InvalidMoveError | AmbiguousMoveError

def verified_styles(pgn: list[str], styles: Styles) -> Either[ChessError, list[str]]:
  """Apply `styles` but keeping track of the current position, so that the captured piece can be used"""
  board = chess.Board()
  moves = []
  try:
    for san in pgn:
      move = board.parse_san(san)
      moves.append(style(san, styles, captured_piece(board, move)))
      board.push(move)
    return Right(moves)
  except (IllegalMoveError, InvalidMoveError, AmbiguousMoveError) as e:
    return Left(e)
  
def apply_styles(pgn: list[str], styles: Styles | None, verify_legal: bool = True) -> Either[ChessError, list[str]]:
  """Apply `styles` to `pgn`. If some style required a captured piece (or `verify_legal`), the game position is kept track of"""
  if styles is None:
    return Right(pgn)
  elif styles.pawn_capture == 'PxN' or styles.piece_capture == 'NxN' or verify_legal:
    return verified_styles(pgn, styles)
  else:
    return Right([style(san, styles) for san in pgn])

def export(pgn: list[str], ann: Annotations) -> Either[ChessError, list[str]]:
  """Export `pgn` into `labels` as described by the annotations"""
  moves = pgn if ann.end_correct is None else pgn[:ann.end_correct]
  styled = apply_styles(moves, ann.styles)
  if ann.language is None:
    return styled
  else:
    return styled.fmap(lambda moves: [translate(san, ann.language) for san in moves])

