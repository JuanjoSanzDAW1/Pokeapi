from fastapi import APIRouter
from starlette.responses import HTMLResponse

from handler.fetch_helpers import fetch_water_pokemons

router = APIRouter()


@router.get("/", response_class=HTMLResponse)
def read_root():
    return """
    <html>
        <head>
            <title>Bienvenida</title>
        </head>
        <body>
            <h1>Hola, Victor!</h1>
            <p>Somos el grupo de Juan José, Luis, Erwin, Lucian y Sergio.</p>
        </body>
    </html>
    """


@router.get("/water_pokemons", response_class=HTMLResponse)
def get_water_pokemons():
    pokemons = fetch_water_pokemons()
    if not pokemons:
        return """
        <html>
            <body>
                <h1>No se encontraron Pokémon de tipo agua.</h1>
            </body>
        </html>
        """

    pokemon_list = "".join([f"<li>{name}</li>" for name in pokemons])
    return f"""
    <html>
        <head>
            <title>Water Pokémons</title>
        </head>
        <body>
            <h1>Lista de Pokémon de tipo Agua</h1>
            <ul>{pokemon_list}</ul>
        </body>
    </html>
    """
