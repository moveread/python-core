from moveread.core import CoreAPI, ImageID, SheetID
from . import ops

class ImagesAPI:

  def __init__(self, core: CoreAPI):
    self._core = core

  async def upsert(self, id: SheetID, img: bytes, *, version: int | None = None):
    """Insert an image. If `version` is specified, replaces a current image. Otherwise it is appended"""
    return await ops.upsert(id, img, version=version, api=self._core)

  async def annotate(self, id: ImageID, schema: str, meta):
    return await ops.annotate(id, schema, meta, api=self._core)