import haskellian.either as E
from scoresheet_models import Model
import pure_cv as vc
from cv2 import Mat
from moveread.core import Image, CoreAPI
from moveread.annotations.images import ImageMeta
from moveread.boxes import export
from moveread.errors import MissingMeta, InvalidData, DBError, InexistentItem

BoxesErr = InvalidData | DBError | InexistentItem | MissingMeta

async def boxes(
  image: Image, model: Model | None = None, *, api: CoreAPI
) -> E.Either[BoxesErr, list[Mat]]:
  try:
    meta = E.validate(image.meta, ImageMeta).mapl(lambda e: InvalidData(e)).unsafe()
    img = (await api.blobs.read(image.url)).unsafe()
    mat = vc.decode(img)
    return export(mat, meta, model=model)
  except E.IsLeft as e:
    return E.Left(e.value)