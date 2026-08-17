from sqlalchemy.orm import Session

from app.repositories.season_repository import SeasonRepository
from app.schemas.season import SeasonCreate, SeasonUpdate


class SeasonService:

    @staticmethod
    def get_all(db: Session):
        return SeasonRepository(db).get_all()

    @staticmethod
    def get_by_id(db: Session, season_id: int):
        return SeasonRepository(db).get_by_id(season_id)

    @staticmethod
    def create(db: Session, season: SeasonCreate):
        return SeasonRepository(db).create(season)

    @staticmethod
    def update(db: Session, season_id: int, season: SeasonUpdate):
        return SeasonRepository(db).update(season_id, season)

    @staticmethod
    def delete(db: Session, season_id: int):
        return SeasonRepository(db).delete(season_id)