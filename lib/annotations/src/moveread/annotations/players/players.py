from pydantic import ConfigDict
import haskellian.either as E
from moveread.labels import Annotations

class PlayerMeta(Annotations):
  model_config = ConfigDict(extra='allow')
