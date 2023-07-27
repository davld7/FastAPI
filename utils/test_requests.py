# pip install rich
import requests
from rich.console import Console

url = "https://fastapi-1-v7692141.deta.app/"
response = requests.get(url)

console = Console()

if response.status_code == 200:
    data = response.json()
    team_members = data["full_stack_team"]
    console.print("\n[bold blue]Integrantes del equipo Full-Stack:[bold blue]\n")
    for member in team_members:
        console.print("- [green]" + member + ".[green]")
else:
    console.print(f"Error al obtener los datos del API. Código de estado: [bold red]{response.status_code}[/bold red]")
