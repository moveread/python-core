from pydantic import ConfigDict
from moveread.labels import Annotations, Styles

class PlayerMeta(Annotations):
  model_config = ConfigDict(extra='allow')
