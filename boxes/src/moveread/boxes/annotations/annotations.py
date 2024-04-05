from pydantic import BaseModel
from .types import Rectangle

class Annotations(BaseModel):
  model_coords: Rectangle
  """Grid coords (matching some scoresheet model)"""