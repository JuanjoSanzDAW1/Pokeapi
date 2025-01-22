from fastapi import APIRouter
from handler.water_pokemons_handler import router as water_router







router = APIRouter()


router.include_router(water_router)
