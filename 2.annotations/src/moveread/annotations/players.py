from pydantic import ConfigDict
from moveread.labels import Annotations as PlayerAnnotations, Styles, Language

class PlayerMeta(PlayerAnnotations):
  model_config = ConfigDict(extra='allow')
