from typing import Literal
from pydantic import BaseModel, RootModel
from chess_notation.language import Language
from chess_notation.styles import Check, Mate, Castle, PawnCapture, PieceCapture

NA = Literal['N/A']
"""Not Applicable"""

class Styles(BaseModel):
  """Like `chess_notation.Styles`, but with possibly `'N/A'` annotations"""
  check: Check | NA | None = None
  mate: Mate | NA | None = None
  castle: Castle | NA | None = None
  pawn_capture: PawnCapture | NA | None = None
  piece_capture: PieceCapture | NA | None = None

class Annotations(BaseModel):
  language: Language | NA | None = None
  styles: Styles | None = None
  end_correct: int | None = None
  manual_labels: dict[int, str] | None = None

AnnotationSchemas = dict(
  language=RootModel[Language],
  style=Styles,
  end_correct=RootModel[int],
  manual_labels=RootModel[dict[int, str]]
)
