from typing import NamedTuple
import haskellian.either as E
from cv2 import Mat
from moveread.core import Player, CoreAPI
from moveread.errors import InvalidData
from . import export_boxes, export_labels, BoxesErr, ChessError

class Sample(NamedTuple):
  box: Mat
  label: str

class SamplesOk(NamedTuple):
  samples: list[list[Sample]]
  """Ply-major samples (may have multiple samples per ply if a sheet has multiple image versions)"""
  box_errors: list[InvalidData | list[BoxesErr]]

SamplesResult = E.Either[InvalidData|ChessError, SamplesOk]

def format_samples(
  boxes: list[list[Mat]],
  labels: list[str]
) -> list[list[Sample]]:
  return [
    [Sample(b, lab) for b in bxs]
    for bxs, lab in zip(boxes, labels)
  ]

async def export_samples(player: Player, pgn: list[str], *, api: CoreAPI) -> SamplesResult:
  try:
    labels = export_labels(player, pgn).unsafe()
    r = await export_boxes(player, api=api)
    samples = format_samples(r.boxes, labels)
    return E.Right(SamplesOk(samples, r.errors))
  except E.IsLeft as e:
    return E.Left(e.value)