from sqlalchemy.orm import Session

from app.models.season import Season
from app.schemas.season import SeasonCreate, SeasonUpdate


class SeasonRepository:

    def __init__(self, db: Session):
        self.db = db

    def get_all(self):
        return self.db.query(Season).all()

    def get_by_id(self, season_id: int):
        return (
            self.db.query(Season)
            .filter(Season.id == season_id)
            .first()
        )

    def create(self, season_data: SeasonCreate):
        season = Season(**season_data.model_dump())

        self.db.add(season)
        self.db.commit()
        self.db.refresh(season)

        return season

    def update(self, season_id: int, season_data: SeasonUpdate):

        season = self.get_by_id(season_id)

        if not season:
            return None

        update_data = season_data.model_dump(exclude_unset=True)

        for key, value in update_data.items():
            setattr(season, key, value)

        self.db.commit()
        self.db.refresh(season)

        return season

    def delete(self, season_id: int):

        season = self.get_by_id(season_id)

        if not season:
            return False

        self.db.delete(season)
        self.db.commit()

        return True