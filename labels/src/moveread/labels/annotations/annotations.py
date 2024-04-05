from pydantic import BaseModel
from chess_notation.language import Language
from chess_notation.styles import Styles

class Annotations(BaseModel):
  language: Language | None = None
  styles: Styles | None = None
  end_correct: int | None = None
