import asyncio
import haskellian.either as E
from cv2 import Mat
from scoresheet_models import models
from moveread.core import Sheet, CoreAPI
from moveread.annotations.sheets import SheetMeta
from moveread.errors import InvalidData
from ..images import boxes as image_boxes, BoxesErr

BoxesResult = E.Either[InvalidData, list[E.Either[BoxesErr, list[Mat]]]]

async def boxes(
  sheet: Sheet, *, api: CoreAPI
) -> BoxesResult:
  try:
    meta = E.validate(sheet.meta or {}, SheetMeta).mapl(lambda e: InvalidData(e)).unsafe()
    model = meta.model and models[meta.model]
    tasks = [image_boxes(img, model, blobs=api.blobs) for img in sheet.images]
    return E.Right(await asyncio.gather(*tasks))
  except E.IsLeft as e:
    return E.Left(e.value)