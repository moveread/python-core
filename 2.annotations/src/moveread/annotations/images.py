from typing import Literal
from pydantic import ConfigDict
from moveread.boxes import Annotations as ImageAnnotations, Contours, Rectangle
from robust_extraction import Corners

Source = Literal['raw-scan', 'corrected-scan', 'camera', 'corrected-camera', 'robust-corrected'] 

class ImageMeta(ImageAnnotations):
  model_config = ConfigDict(extra='allow')
  source: Source | None = None
  perspective_corners: Corners | None = None
