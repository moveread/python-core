from pydantic import BaseModel, RootModel
from chess_notation.language import Language
from chess_notation.styles import Styles

class Annotations(BaseModel):
  language: Language | None = None
  styles: Styles | None = None
  end_correct: int | None = None
  manual_labels: dict[int, str] | None = None

AnnotationSchemas = dict(
  language=RootModel[Language],
  style=Styles,
  end_correct=RootModel[int],
  manual_labels=RootModel[dict[int, str]]
)
