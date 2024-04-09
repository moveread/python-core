from typing import Literal
from pydantic import BaseModel
from robust_extraction.contours.rois import Contours
from .types import Rectangle

RobustExtractionResult = Literal['failed', 'incorrect', 'perspective-correct', 'correct']
"""`'perspective-correct'` is when the corrected image is good but the contours are bad"""

class Annotations(BaseModel):
  grid_coords: Rectangle | None = None
  """Grid coords (matching some scoresheet model)"""
  box_contours: Contours | None = None
  """Explicit box contours (given by robust-extraction, probably)"""
  robust_extraction: RobustExtractionResult | None = None