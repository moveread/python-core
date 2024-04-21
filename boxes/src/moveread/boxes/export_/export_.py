from typing import Unpack, TypedDict, NotRequired, Literal
from cv2 import Mat
import numpy as np
import haskellian.either as E
from scoresheet_models import Model
from robust_extraction import extract_contours
from ..annotations import Annotations
from .model import extract_grid, Pads
from moveread.errors import MissingMeta

class Params(TypedDict):
  model: NotRequired[Model|None]
  pads: NotRequired[Pads|None]


def export(img: Mat|np.ndarray, ann: Annotations, **params: Unpack[Params]) -> E.Either[MissingMeta, list[Mat]]:
  """Export an image's boxes"""
  if ann.box_contours is not None:
    return E.Right(extract_contours(img, ann.box_contours))
  if ann.grid_coords is None:
    return E.Left(MissingMeta('No `box_contours` nor `grid_coords` provided'))
  if params.get('model') is None:
    return E.Left(MissingMeta('Model parameter required when relying on `grid_coords`'))
  return E.Right(extract_grid(img=img, coords=ann.grid_coords, **params))