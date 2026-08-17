from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.schemas.episode import (
    EpisodeCreate,
    EpisodeUpdate,
    EpisodeResponse,
)
from app.services.episode_service import EpisodeService

router = APIRouter()


@router.get("/", response_model=list[EpisodeResponse])
def get_episodes(db: Session = Depends(get_db)):
    service = EpisodeService(db)
    return service.get_all()


@router.get("/{episode_id}", response_model=EpisodeResponse)
def get_episode(episode_id: int, db: Session = Depends(get_db)):
    service = EpisodeService(db)

    episode = service.get_by_id(episode_id)

    if not episode:
        raise HTTPException(status_code=404, detail="Episode not found")

    return episode


@router.post("/", response_model=EpisodeResponse, status_code=201)
def create_episode(
    episode: EpisodeCreate,
    db: Session = Depends(get_db),
):
    service = EpisodeService(db)
    return service.create(episode)


@router.put("/{episode_id}", response_model=EpisodeResponse)
def update_episode(
    episode_id: int,
    episode: EpisodeUpdate,
    db: Session = Depends(get_db),
):
    service = EpisodeService(db)

    updated = service.update(episode_id, episode)

    if not updated:
        raise HTTPException(status_code=404, detail="Episode not found")

    return updated


@router.delete("/{episode_id}")
def delete_episode(
    episode_id: int,
    db: Session = Depends(get_db),
):
    service = EpisodeService(db)

    deleted = service.delete(episode_id)

    if not deleted:
        raise HTTPException(status_code=404, detail="Episode not found")

    return {"message": "Episode deleted successfully"}