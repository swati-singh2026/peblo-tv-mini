from typing import List

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.schemas.season import (
    SeasonCreate,
    SeasonUpdate,
    SeasonResponse,
)
from app.services.season_service import SeasonService

router = APIRouter()



@router.get("/", response_model=List[SeasonResponse])
def get_all_seasons(db: Session = Depends(get_db)):
    return SeasonService.get_all(db)


@router.get("/{season_id}", response_model=SeasonResponse)
def get_season(season_id: int, db: Session = Depends(get_db)):
    season = SeasonService.get_by_id(db, season_id)

    if not season:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Season not found",
        )

    return season


@router.post(
    "/",
    response_model=SeasonResponse,
    status_code=status.HTTP_201_CREATED,
)
def create_season(
    season: SeasonCreate,
    db: Session = Depends(get_db),
):
    return SeasonService.create(db, season)


@router.put("/{season_id}", response_model=SeasonResponse)
def update_season(
    season_id: int,
    season: SeasonUpdate,
    db: Session = Depends(get_db),
):
    updated = SeasonService.update(db, season_id, season)

    if not updated:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Season not found",
        )

    return updated


@router.delete("/{season_id}")
def delete_season(
    season_id: int,
    db: Session = Depends(get_db),
):
    deleted = SeasonService.delete(db, season_id)

    if not deleted:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Season not found",
        )

    return {
        "message": "Season deleted successfully"
    }
