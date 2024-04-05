from typing import Unpack
from cv2 import Mat
from .model import extract, Params as ModelParams


# possibly will have more overloads in the future
def export(img: Mat, **params: Unpack[ModelParams]) -> list[Mat]:
  """Export an image's boxes"""
  return extract(img, **params)