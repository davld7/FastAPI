from typing import Dict, List


def anime_schema(anime) -> Dict:
    return {"id": str(anime["_id"]),
            "name": anime["name"],
            "description": anime["description"],
            "episodes": anime["episodes"],
            "season": anime["season"],
            "genres": anime["genres"],
            "image_url": anime["image_url"]}


def animes_schema(animes) -> List:
    return [anime_schema(anime) for anime in animes]
