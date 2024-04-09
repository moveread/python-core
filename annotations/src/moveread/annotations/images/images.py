from typing import Literal, Any
from pydantic import ConfigDict
import haskellian.either as E
from moveread.boxes import Annotations

Source = Literal['raw-scan', 'corrected-scan', 'camera', 'corrected-camera', 'robust-corrected'] 

class ImageMeta(Annotations):
  model_config = ConfigDict(extra='allow')
  source: Source | None = None
