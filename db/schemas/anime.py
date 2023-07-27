def anime_schema(anime) -> dict:
    return {"id": str(anime["_id"]),
            "name": str(anime["name"]),
            "description": str(anime["description"]),
            "episodes": int(anime["episodes"]),
            "season": str(anime["season"]),
            "genres": str(anime["genres"]),
            "image_url": str(anime["image_url"])}


def animes_schema(animes) -> list:
    return sorted([anime_schema(anime) for anime in animes], key=lambda x: x['name'].lower())
