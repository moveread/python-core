from typing import Literal
from pydantic import BaseModel
from robust_extraction.contours.rois import Contours
from .types import Rectangle

class Annotations(BaseModel):
  grid_coords: Rectangle | None = None
  """Grid coords (matching some scoresheet model)"""
  box_contours: Contours | None = None
  """Explicit box contours (given by robust-extraction, probably)"""
  robust_extraction: Literal['failed', 'incorrect', 'imprecise', 'correct'] | None = None
  """Result of box-extraction. Incorrect/imprecise/correct is subjective"""