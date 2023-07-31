from fastapi import APIRouter, HTTPException, status
from db.models.anime import Anime, AnimeToCreate
from db.schemas.anime import anime_schema, animes_schema
from db.client import animes_collection
from bson import ObjectId
from pymongo.errors import PyMongoError

router = APIRouter(prefix="/animes",
                   tags=["animes"],
                   responses={status.HTTP_404_NOT_FOUND: {"message": "No encontrado."}})


@router.get("/", response_model=list[Anime])
async def animes():
    return animes_schema(animes_collection.find())


def search_anime(field: str, key):
    try:
        anime = animes_collection.find_one({field: key})
        return Anime(**anime_schema(anime))
    except:
        return {"error": "No se ha encontrado el anime."}


@router.get("/search_id/{id}")  # Path
async def anime(id: str):
    return search_anime("_id", ObjectId(id))


@router.get("/search_id/")  # Query
async def anime(id: str):
    return search_anime("_id", ObjectId(id))


@router.get("/search/{name}")  # Path
async def anime(name: str):
    return search_anime("name", name)


@router.get("/search/")  # Query
async def anime(name: str):
    return search_anime("name", name)


@router.post("/", response_model=Anime, status_code=status.HTTP_201_CREATED)
async def anime(anime: AnimeToCreate):
    if type(search_anime("name", anime.name)) == Anime:
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
    return search_anime("_id", ObjectId(anime.id))


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
