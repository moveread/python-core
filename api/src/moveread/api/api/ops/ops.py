from typing import Annotated
from fastapi import APIRouter, File
from pydantic import BaseModel
from haskellian.either import Either
import pure_cv as vc
import robust_extraction as re
from robust_extraction.contours.rois import Contours
from robust_extraction import templates as ts

class Result(BaseModel):
  contours: Contours
  contoured_image: str
  corrected_image: str

router = APIRouter()

def make_result(res: re.Result) -> Result:
  corr = vc.b64encode(res.corr_img, '.jpg', url_safe=False)
  contoured_mat = vc.draw.contours(res.contours, res.corr_img)
  contoured = vc.b64encode(contoured_mat, '.jpg', url_safe=False)
  return Result(contours=res.contours, contoured_image=contoured, corrected_image=corr)

@router.post('/extract/')
def extract(sheet: Annotated[bytes, File()], model: ts.ModelID, descale_height: int | None = None) -> Either[re.Error, Result]:
  mat = vc.decode(sheet)
  if descale_height is None:
    res = re.extract(mat, ts.models[model])
  else:
    res = re.descaled_extract(mat, ts.models[model], descale_h=descale_height)

  return res | make_result