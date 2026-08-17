from fastapi import APIRouter

from app.api.v1.endpoints.shows import router as shows_router
from app.api.v1.endpoints.seasons import router as seasons_router
from app.api.v1.endpoints.episodes import router as episodes_router
from app.api.v1.endpoints.artwork import router as artwork_router

api_router = APIRouter()

api_router.include_router(shows_router, prefix="/shows", tags=["Shows"])
api_router.include_router(seasons_router, prefix="/seasons", tags=["Seasons"])
api_router.include_router(episodes_router, prefix="/episodes", tags=["Episodes"])
api_router.include_router(artwork_router, prefix="/artwork", tags=["Artwork"])
