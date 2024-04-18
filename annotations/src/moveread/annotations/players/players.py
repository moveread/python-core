from pydantic import ConfigDict
from moveread.labels import Annotations

class PlayerMeta(Annotations):
  model_config = ConfigDict(extra='allow')
