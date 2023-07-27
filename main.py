# FastAPI

# Official Documentation https://fastapi.tiangolo.com/

# pip install "fastapi[all]"
# py -3.11 -m pip install "fastapi[all]"
# py -3.11 -m pip install --upgrade "fastapi[all]"

# Uvicorn

# Start Server
# uvicorn main:app --reload
# http://127.0.0.1:8000

# Stop Server: CTRL + C

# Documentation

# Swagger http://127.0.0.1:8000/docs
# Redocly http://127.0.0.1:8000/redoc

from fastapi import FastAPI
from routers import animes
from fastapi.staticfiles import StaticFiles
# products, users, basic_auth_users, jwt_auth_users, users_db, animes
app = FastAPI()

# Routers

# app.include_router(products.router)
# app.include_router(users.router)
# app.include_router(basic_auth_users.router)
# app.include_router(jwt_auth_users.router)
# app.include_router(users_db.router)
app.include_router(animes.router)

# Static Files

app.mount("/static", StaticFiles(directory="static"), name="static")
# http://127.0.0.1:8000/static/lucy.jpg


@app.get("/")
async def root():
    return {"full_stack_team": ["Roberto David Morales Ramos",
                                "Byron Steven Flores Gaitán",
                                "Brandon Isaac Cruz Reyes",
                                "Jonathan Josué Downs Cruz"]}


# http://127.0.0.1:8000/url

@app.get("/url")
async def url():
    return {"url": "https://github.com/davld7"}
