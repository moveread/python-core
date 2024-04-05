# Moveread Labels

> Annotating and exporting labels

## Usage

```python
from moveread.labels import Annotations, Styles, export

ann = Annotations(language='DE', styles=Styles(pawn_capture='de', piece_capture='NxN'))
export(['e4', 'e5', 'Nf3', 'Nc6', 'd4', 'exd4', 'Nxd4', 'Nf6', 'Nxc6', 'bxc6'], ann)
# Right(value=['e4', 'e5', 'Sf3', 'Sc6', 'd4', 'ed', 'SxB', 'Sf6', 'SxS', 'bc'])

export(['e4', 'e4'], ann)
# Left(value=IllegalMoveError("illegal san: 'e4' in rnbqkbnr/[...]"))
```