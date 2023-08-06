from fastapi import APIRouter, HTTPException, status, Path
from db.models.anime import Anime, AnimeToCreate
from db.schemas.anime import anime_schema, animes_schema
from db.client import animes_collection
from bson import ObjectId
from pymongo.errors import PyMongoError
from typing import List

router = APIRouter(prefix="/animes",
                   tags=["animes"],
                   responses={status.HTTP_404_NOT_FOUND: {"error": "Not found."}})

# Specify the collation with the case insensitive sort order option
collation = {'locale': 'en', 'strength': 2}

# Sort the collection by the "name" field using collation
sort = [("name", 1)]


@router.get("/", response_model=List[Anime])
async def get_animes():
    """
    Get all the animes.

    Returns:
    - `List[Anime]`: List of animes.
    """
    animes = animes_collection.find().collation(collation).sort(sort)
    return animes_schema(animes)


def find_anime(key, value):
    """
    Find anime by key and value.

    Parameters:
    - `key`: Key.
    - `value`: Value.

    Returns:
    - `Anime`: Anime.

    Raises:
    - `HTTPException`: If anime not found.
    """
    anime = animes_collection.find_one({key: value})
    if anime:
        return Anime(**anime_schema(anime))
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail={
                            "error": "Anime not found."})


# Path

@router.get("/id/{id}", response_model=Anime, status_code=status.HTTP_200_OK)
async def anime(id: str = Path(..., min_length=24, max_length=24, regex="^[0-9a-fA-F]{24}$", description="Id of the anime")):
    """
    Get anime by id.

    Parameters:
    - `id`: Id of the anime.

    Returns:
    - `Anime`: Anime.

    Raises:
    - `HTTPException`: If anime not found.
    """
    return find_anime("_id", ObjectId(id))


@router.get("/name/{name}", response_model=Anime, status_code=status.HTTP_200_OK)
async def anime(name: str = Path(..., description="Name of the anime")):
    """
    Get anime by name.

    Parameters:
    - `name`: Name of the anime.

    Returns:
    - `Anime`: Anime.

    Raises:
    - `HTTPException`: If anime not found.
    """
    return find_anime("name", name)


# Query

# @router.get("/search_id/")
# async def anime(id: str):
#     return find_anime("_id", ObjectId(id))


# @router.get("/search/")
# async def anime(name: str):
#     return find_anime("name", name)


@router.post("/", response_model=Anime, status_code=status.HTTP_201_CREATED)
async def anime(anime: AnimeToCreate):
    if type(find_anime("name", anime.name)) == Anime:
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, detail="El anime ya existe.")
    anime_dict = dict(anime)
    id = animes_collection.insert_one(anime_dict).inserted_id
    new_anime = anime_schema(animes_collection.find_one({"_id": id}))
    return Anime(**new_anime)


@router.put("/", response_model=Anime)
async def anime(anime: Anime):
    anime_dict = dict(anime)
    del anime_dict["id"]
    try:
        animes_collection.find_one_and_replace(
            {"_id": ObjectId(anime.id)}, anime_dict)
    except:
        return {"error": "No se actualizó el anime."}
    return find_anime("_id", ObjectId(anime.id))


@router.delete("/{id}", status_code=status.HTTP_200_OK)
async def delete_anime(id: str):
    try:
        obj_id = ObjectId(id)
    except:
        raise HTTPException(status_code=400, detail="Identificador inválido.")

    try:
        found = animes_collection.find_one_and_delete({"_id": obj_id})
    except PyMongoError:
        raise HTTPException(
            status_code=500, detail="Error al buscar y eliminar el anime.")

    if not found:
        raise HTTPException(
            status_code=404, detail="No se encontró el anime a borrar.")
    else:
        return {"message": "Se ha borrado el anime."}
