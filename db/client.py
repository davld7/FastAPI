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
from environment import settings

# Base de datos local
# db_client = MongoClient().local

# Base de datos remota

# MongoDB Atlas

# FastAPI Cluster

# Create a new client and connect to the server
client = MongoClient(settings.mongodb_uri, server_api=ServerApi('1'))

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as exception:
    print(exception)

db = client.get_database("fastapi")
animes_collection = db.get_collection("animes")
