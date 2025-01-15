from fastapi import APIRouter
from handler.water_pokemons_handler import router as water_router






# Crea un nuevo APIRouter
router = APIRouter()

# Incluyendo las rutas desde handler
router.include_router(water_router)
