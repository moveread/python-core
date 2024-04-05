from typing import Unpack, TypedDict, NotRequired, Literal
from cv2 import Mat
import haskellian.either as E
from dataclasses import dataclass
from scoresheet_models import Model
from ..annotations import Annotations
from .model import extract, Pads

class Params(TypedDict):
  model: NotRequired[Model]
  pads: NotRequired[Pads]

@dataclass
class MissingAnnotations(BaseException):
  detail: str
  reason: Literal['missing-annotations'] = 'missing-annotations'

def export(img: Mat, ann: Annotations, **params: Unpack[Params]) -> E.Either[MissingAnnotations, list[Mat]]:
  """Export an image's boxes"""
  if ann.grid_coords is None:
    return E.Left(MissingAnnotations(detail='No `grid_coords` provided'))
  if not 'model' in params:
    return E.Left(MissingAnnotations(detail='Model parameter required when relying on `grid_coords`'))
  return E.Right(extract(img, coords=ann.grid_coords, **params))