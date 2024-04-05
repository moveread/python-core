# Moveread Boxes

> Annotating and exporting boxes

## Usage

```python
import cv2 as cv
from scoresheet_models import models
from moveread.boxes import Annotations, export, Rectangle

sheet = cv.imread('../.dev/images/models/fcde/xl.jpg')
ann = Annotations(grid_coords=Rectangle(tl=(0.05, 0.195), size=(0.935, 0.66)))
boxes = export(sheet, ann, model=models['fcde'])
# Rigth(value=[cv.Mat(...), ...])

export(sheet, ann)
# Left(value=MissingAnnotations(detail='Model parameter required when relying on `grid_coords`'))

export(sheet, ann=Annotations())
# Left(value=MissingAnnotations(detail='No `grid_coords` provided'))
```