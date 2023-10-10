## MongoDB Client ##

# Descarga versión community: https://www.mongodb.com/try/download
# Instalación:https://www.mongodb.com/docs/manual/tutorial
# Módulo conexión MongoDB: pip install pymongo
# Iniciar servicio: net start MongoDB
# Detener servicio: net stop MongoDB
# Extensión: MongoDB for VS Code
# Conexión: mongodb://localhost

from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from environment import variables

# Base de datos local
# db_client = MongoClient().local

# Base de datos remota

# MongoDB Atlas

# FastAPI Cluster

# Create a new client and connect to the server
client = MongoClient(variables.uri, server_api=ServerApi('1'))

db = client.get_database("fastapi")
animes_collection = db.get_collection("animes")
