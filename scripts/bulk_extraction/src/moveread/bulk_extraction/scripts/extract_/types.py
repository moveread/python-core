from typing import Any
from dataclasses import dataclass
from pydantic import BaseModel
from haskellian.either import Either
from robust_extraction.contours.rois import Contours
from moveread.core import ImageID
from moveread.annotations.images import ImageMeta
from robust_extraction.templates import ModelID

class Result(BaseModel):
  contours: Contours
  corrected_url: str
  contoured_url: str

class ExtractMeta(ImageMeta):
  robust_extract_result: Either[Any, Result] | None = None

@dataclass
class ExtractTask:
  img: bytes
  modelId: ModelID
  imageId: ImageID