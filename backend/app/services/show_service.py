from sqlalchemy.orm import Session

from app.repositories.show_repository import ShowRepository
from app.schemas.show import ShowCreate, ShowUpdate


class ShowService:

    @staticmethod
    def get_all(db: Session):
        return ShowRepository.get_all(db)

    @staticmethod
    def get_by_id(db: Session, show_id: int):
        return ShowRepository.get_by_id(db, show_id)

    @staticmethod
    def create(db: Session, show: ShowCreate):
        return ShowRepository.create(db, show)

    @staticmethod
    def update(db: Session, db_show, show: ShowUpdate):
        return ShowRepository.update(db, db_show, show)

    @staticmethod
    def delete(db: Session, db_show):
        return ShowRepository.delete(db, db_show)
    