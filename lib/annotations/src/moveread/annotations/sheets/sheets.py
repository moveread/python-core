from typing import Any
from pydantic import BaseModel, ConfigDict
import haskellian.either as E
from scoresheet_models import ModelID

class SheetMeta(BaseModel):
  model_config = ConfigDict(extra='allow')
  model: ModelID | None = None
