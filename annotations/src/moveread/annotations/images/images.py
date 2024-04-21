from typing import Literal
from pydantic import ConfigDict
from moveread.boxes import Annotations
from robust_extraction.manual._correct import Corners

Source = Literal['raw-scan', 'corrected-scan', 'camera', 'corrected-camera', 'robust-corrected'] 

class ImageMeta(Annotations):
  model_config = ConfigDict(extra='allow')
  source: Source | None = None
  perspective_corners: Corners | None = None
