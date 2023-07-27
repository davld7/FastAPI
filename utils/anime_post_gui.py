import tkinter as tk
import requests
import json


def submit():
    # Obtener los valores de los campos de entrada
    name = name_entry.get()
    description = description_entry.get()
    episodes = int(episodes_entry.get())
    season = season_entry.get()
    genres = genres_entry.get()
    image_url = image_url_entry.get()

    # Crear un diccionario con los valores ingresados por el usuario
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

    # Agregar mensaje si la respuesta es 201 created
    if response.status_code == 201:
        # Eliminar label existente si es que hay alguno
        if hasattr(window, "response_message"):
            window.response_message.pack_forget()
        # Parsear respuesta a objeto json
        anime_dict = json.loads(response.content)
        # Asignar el ID al campo de entrada de texto
        id_entry.delete(0, tk.END)
        id_entry.insert(
            0, f'https://fastapi-1-v7692141.deta.app/animes/search_id/{anime_dict["id"]}')
        # Crear nuevo label con mensaje de éxito
        response_message = tk.Label(
            window, text="Anime added successfully!", font=("Arial", 16), fg="green")
        response_message.pack()
        window.response_message = response_message

    # Agregar mensaje si el código de estado es 422 Validation Error
    elif response.status_code == 422:
        # Eliminar label existente si es que hay alguno
        if hasattr(window, "response_message"):
            window.response_message.pack_forget()
        # Crear nuevo label con mensaje de error
        response_message = tk.Label(
            window, text="Validation Error. Please check your data!", font=("Arial", 16), fg="red")
        response_message.pack()
        window.response_message = response_message

    # Agregar mensaje si el código de estado es 404 Not Found
    elif response.status_code == 422:
        # Eliminar label existente si es que hay alguno
        if hasattr(window, "response_message"):
            window.response_message.pack_forget()
        # Crear nuevo label con mensaje de error
        response_message = tk.Label(
            window, text="Not Found!", font=("Arial", 16), fg="red")
        response_message.pack()
        window.response_message = response_message


def clear():
    # Borrar contenido de todas las cajas de texto
    name_entry.delete(0, tk.END)
    description_entry.delete(0, tk.END)
    episodes_entry.delete(0, tk.END)
    season_entry.delete(0, tk.END)
    genres_entry.delete(0, tk.END)
    image_url_entry.delete(0, tk.END)
    # Eliminar label existente si es que hay alguno
    if hasattr(window, "response_message"):
        window.response_message.pack_forget()
    # Borrar ID del campo de entrada de texto
    id_entry.delete(0, tk.END)
    name_entry.focus_set()


# Crear una ventana
window = tk.Tk()
window.title("Anime Post - Full Stack Team API")
window.geometry("550x550")
window.attributes('-topmost', True)


def focus_on_window():
    window.attributes('-topmost', True)
    window.after(100, focus_on_window)


focus_on_window()

# Crear campos de entrada de texto para cada clave en el diccionario de anime
name_label = tk.Label(window, text="Name:", font=("Arial", 16))
name_label.pack()
name_entry = tk.Entry(window, font=("Arial", 16))
name_entry.pack(ipadx=100)

description_label = tk.Label(window, text="Description:", font=("Arial", 16))
description_label.pack()
description_entry = tk.Entry(window, font=("Arial", 16))
description_entry.pack(ipadx=100)

episodes_label = tk.Label(window, text="Episodes:", font=("Arial", 16))
episodes_label.pack()
episodes_entry = tk.Entry(window, font=("Arial", 16))
episodes_entry.pack(ipadx=100)

season_label = tk.Label(window, text="Season:", font=("Arial", 16))
season_label.pack()
season_entry = tk.Entry(window, font=("Arial", 16))
season_entry.pack(ipadx=100)

genres_label = tk.Label(window, text="Genres:", font=("Arial", 16))
genres_label.pack()
genres_entry = tk.Entry(window, font=("Arial", 16))
genres_entry.pack(ipadx=100)

image_url_label = tk.Label(window, text="Image URL:", font=("Arial", 16))
image_url_label.pack()
image_url_entry = tk.Entry(window, font=("Arial", 16))
image_url_entry.pack(ipadx=100)

submit_button = tk.Button(window, text="Submit",
                          command=submit, font=("Arial", 16))
submit_button.pack()

clear_button = tk.Button(window, text="Clear",
                         command=clear, font=("Arial", 16))
clear_button.pack()

id_label = tk.Label(window, text="Get Anime Detail:", font=("Arial", 16))
id_label.pack()
id_entry = tk.Entry(window, font=("Arial", 16))
id_entry.pack(ipadx=100)

# Iniciar el bucle principal de la ventana
window.mainloop()
