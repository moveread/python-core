from pydantic import BaseModel
from .types import Rectangle

class Annotations(BaseModel):
  grid_coords: Rectangle | None = None
  """Grid coords (matching some scoresheet model)"""