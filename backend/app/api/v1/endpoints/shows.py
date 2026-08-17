from typing import List

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.schemas.show import (
    ShowCreate,
    ShowUpdate,
    ShowResponse,
)
from app.services.show_service import ShowService

router = APIRouter(tags=["Shows"])


@router.get("/", response_model=List[ShowResponse])
def get_shows(db: Session = Depends(get_db)):
    return ShowService.get_all(db)


@router.get("/{show_id}", response_model=ShowResponse)
def get_show(show_id: int, db: Session = Depends(get_db)):
    show = ShowService.get_by_id(db, show_id)

    if not show:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Show not found",
        )

    return show


@router.post(
    "/",
    response_model=ShowResponse,
    status_code=status.HTTP_201_CREATED,
)
def create_show(
    show: ShowCreate,
    db: Session = Depends(get_db),
):
    return ShowService.create(db, show)


@router.put("/{show_id}", response_model=ShowResponse)
def update_show(
    show_id: int,
    show: ShowUpdate,
    db: Session = Depends(get_db),
):
    updated = ShowService.update(db, show_id, show)

    if not updated:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Show not found",
        )

    return updated


@router.delete("/{show_id}")
def delete_show(
    show_id: int,
    db: Session = Depends(get_db),
):
    deleted = ShowService.delete(db, show_id)

    if not deleted:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Show not found",
        )

    return {
        "message": "Show deleted successfully"
    }
