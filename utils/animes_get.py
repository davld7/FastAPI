import requests

url = "https://fastapi-1-v7692141.deta.app/animes/"

response = requests.get(url)

if response.status_code == 200:

    animes_json = response.json()
    
    print(f"Cantidad de animes en la base de datos: {len(animes_json)}\n")

    for anime in animes_json:
        print("ID:", anime["id"])
        print("Nombre:", anime["name"])
        print("Descripción:", anime["description"])
        print("Episodios:", anime["episodes"])
        print("Temporada:", anime["season"])
        print("Géneros:", anime["genres"])
        print("URL de imagen:", anime["image_url"])
        print("------------------------------------")

else:
    print("Error al obtener los datos")
