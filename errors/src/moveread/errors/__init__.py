"""
### Moveread Errors
> Error types for the Moveread Core
"""
from .db import InvalidData, DBError, InexistentItem
from .core import InexistentGame, InexistentPlayer, InexistentSheet
from .annotations import InexistentSchema, MissingMeta, InvalidMeta