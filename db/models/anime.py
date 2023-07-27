from pydantic import BaseModel
from typing import Optional


class Anime(BaseModel):
    id: Optional[str]
    name: str
    description: str
    episodes: int
    season: str
    genres: str
    image_url: str
