from pydantic import BaseModel

class Box(BaseModel):
  url: str
  meta: dict | None = None

class Image(BaseModel):
  url: str
  boxes: list[Box] | None = None
  meta: dict | None = None

class Sheet(BaseModel):
  images: list[Image]
  meta: dict | None = None

class Player(BaseModel):
  sheets: list[Sheet]
  meta: dict | None = None

class Game(BaseModel):
  id: str
  players: list[Player]
  meta: dict | None = None
  