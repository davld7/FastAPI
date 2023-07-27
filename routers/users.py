from fastapi import APIRouter, HTTPException, status
from pydantic import BaseModel

# users_db.py tiene el mismo prefix
router = APIRouter(prefix="/users",
                   tags=["users"],
                   responses={status.HTTP_404_NOT_FOUND: {"message": "No encontrado."}})

# Start Server
# uvicorn users:app --reload

# Entidad user


class User(BaseModel):
    id: int
    name: str
    surname: str
    url: str
    age: int


users_list = [User(id=1, name="name1", surname="surname1", url="no_url", age=20),
              User(id=2, name="name2", surname="surname2", url="no_url", age=10),
              User(id=3, name="name3", surname="surname3", url="no_url", age=17)]

@router.get("/")
async def users():
    return users_list


def search_user(id: int):
    users = filter(lambda user: user.id == id, users_list)
    try:
        return list(users)[0]
    except:
        return {"error": "No se ha encontrado el usuario."}

# Path


@router.get("/search/{id}")  # 127.0.0.1:8000/user/1
async def user(id: int):
    return search_user(id)

# Query


@router.get("/search/")  # 127.0.0.1:8000/user/?id=1
async def user(id: int):
    return search_user(id)


@router.post("/", response_model=User, status_code=status.HTTP_201_CREATED)
async def user(user: User):
    if type(search_user(user.id)) == User:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="El usuario ya existe.")
    users_list.append(user)
    return user


@router.put("/")
async def user(user: User):
    found = False
    for index, saved_user in enumerate(users_list):
        if saved_user.id == user.id:
            users_list[index] = user
            found = True
    if not found:
        return {"error": "No se actualizó el usuario."}
    return user


@router.delete("/{id}")
async def user(id: int):
    found = False
    for index, saved_user in enumerate(users_list):
        if saved_user.id == id:
            del users_list[index]
            found = True
    if not found:
        return {"error": "No se borró el usuario."}
    return {"message": "Se ha borrado el usuario."}
