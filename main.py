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

from fastapi import FastAPI, HTTPException, status
from fastapi.responses import HTMLResponse, FileResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from pymongo.errors import PyMongoError
from db.client import client
from routers import animes

# products, users, basic_auth_users, jwt_auth_users, users_db, animes
app = FastAPI()
app.title = "Anime List API"
app.version = "1.0.0"

# Routers

# app.include_router(products.router)
# app.include_router(users.router)
# app.include_router(basic_auth_users.router)
# app.include_router(jwt_auth_users.router)
# app.include_router(users_db.router)
app.include_router(animes.router)


@app.get("/ping", response_class=JSONResponse, status_code=status.HTTP_200_OK)
async def send_ping():
    try:
        client.admin.command('ping')
        message = "Pinged your deployment. You successfully connected to MongoDB!"
        return JSONResponse(content={"message": message})
    except PyMongoError as exception:
        detail = str(exception)
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=detail)


# Static Files
app.mount("/static/images", StaticFiles(directory="static/images"), name="images")
# http://127.0.0.1:8000/static/images/lucy.jpg


@app.get("/", response_class=HTMLResponse, status_code=status.HTTP_200_OK)
async def index():
    template_path = "templates/index.html"
    media_type = "text/html"
    return FileResponse(template_path, media_type=media_type)


@app.get("/styles.css", tags=["styles"], status_code=status.HTTP_200_OK)
async def styles():
    return FileResponse("static/css/styles.css", media_type="text/css")


@app.get("/script.js", tags=["script"], status_code=status.HTTP_200_OK)
async def script():
    return FileResponse("static/js/script.js", media_type="text/javascript")


@app.get("/logo.png", tags=["logo"], response_class=FileResponse, status_code=status.HTTP_200_OK)
async def logo():
    return FileResponse("static/images/animelist-logo.png", media_type="image/png")


@app.get("/icon.png", tags=["icon"], response_class=FileResponse, status_code=status.HTTP_200_OK)
async def icon():
    return FileResponse("static/images/animelist-icon.png", media_type="image/png")

# @app.get("/")
# async def root():
#     return {"full_stack_team": ["Roberto David Morales Ramos",
#                                 "Byron Steven Flores Gaitán",
#                                 "Brandon Isaac Cruz Reyes",
#                                 "Jonathan Josué Downs Cruz"]}
