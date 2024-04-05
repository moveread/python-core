from typing import Unpack, TypedDict, NotRequired, Literal
from cv2 import Mat
import haskellian.either as E
from scoresheet_models import Model
from ..annotations import Annotations
from .model import extract, Pads
from moveread.errors import MissingMeta

class Params(TypedDict):
  model: NotRequired[Model|None]
  pads: NotRequired[Pads|None]


def export(img: Mat, ann: Annotations, **params: Unpack[Params]) -> E.Either[MissingMeta, list[Mat]]:
  """Export an image's boxes"""
  if ann.grid_coords is None:
    return E.Left(MissingMeta('No `grid_coords` provided'))
  if params.get('model') is None:
    return E.Left(MissingMeta('Model parameter required when relying on `grid_coords`'))
  return E.Right(extract(img=img, coords=ann.grid_coords, **params))