from haskellian import Either, Left, Right
from scoresheet_models import ModelID
import pure_cv as vc
from cv2 import Mat
from kv.api import KV
from moveread.core import ImageMeta
from moveread.boxes import export, exportable
from moveread.errors import MissingMeta

async def image_boxes(
  image: str, meta: ImageMeta | None, model: ModelID | None = None, *, blobs: KV[bytes]
) -> Either[MissingMeta, list[Mat]]:
  if meta is None:
    return Left(MissingMeta('Empty image meta'))
  match exportable(meta, model):
    case Left(err):
      return Left(err)
    case Right(ann):
      img = (await blobs.read(image)).unsafe()
      mat = vc.decode(img)
      return Right(export(mat, ann))