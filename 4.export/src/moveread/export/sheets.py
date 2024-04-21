import asyncio
from haskellian import either as E, iter as I
from cv2 import Mat
from moveread.core import Sheet, CoreAPI
from .images import image_boxes

async def sheet_boxes(sheet: Sheet, *, api: CoreAPI) -> list[list[Mat]]:
  """Returns ply-major boxes (the nested axis corresponds to image version, and thus to the same real box)"""
  model = sheet.meta and sheet.meta.model
  results = await asyncio.gather(*[
    image_boxes(img.url, img.meta, model, blobs=api.blobs)
    for img in sheet.images
  ])
  ok_boxes = E.filter(results)
  return I.transpose_ragged(ok_boxes)