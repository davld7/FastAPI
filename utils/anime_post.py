import requests
import json

name: str = ""
description: str = ""
episodes: int = 0
season: str = ""
genres: str = ""
image_url: str = ""

# Crear un diccionario con los datos a enviar
anime_dict = {
    "name": name,
    "description": description,
    "episodes": episodes,
    "season": season,
    "genres": genres,
    "image_url": image_url
}

# Convertir los datos en formato JSON
anime_json = json.dumps(anime_dict)

# Definir la URL del endpoint de la solicitud POST
url = "https://fastapi-1-v7692141.deta.app/animes/"

# Definir los encabezados de la solicitud POST
anime_headers = {
    "Content-Type": "application/json"
}

# Enviar la solicitud POST con los datos en formato JSON y los encabezados adicionales
response = requests.post(url, data=anime_json, headers=anime_headers)

# Imprimir la respuesta de la solicitud POST
print(response.text)
