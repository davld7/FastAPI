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


def total_animes_pages_schema(total_animes_pages) -> Dict:
    return {"total_animes": total_animes_pages["total_animes"],
            "total_pages": total_animes_pages["total_pages"]}
