from typing_extensions import TypedDict

Vec2 = tuple[float, float]

class Rectangle(TypedDict):
  tl: Vec2
  size: Vec2