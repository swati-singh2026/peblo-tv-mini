from sqlalchemy.orm import Session

from app.repositories.episode_repository import EpisodeRepository
from app.schemas.episode import EpisodeCreate, EpisodeUpdate


class EpisodeService:
    def __init__(self, db: Session):
        self.repository = EpisodeRepository(db)

    def get_all(self):
        return self.repository.get_all()

    def get_by_id(self, episode_id: int):
        return self.repository.get_by_id(episode_id)

    def create(self, episode: EpisodeCreate):
        return self.repository.create(episode)

    def update(self, episode_id: int, episode: EpisodeUpdate):
        return self.repository.update(episode_id, episode)

    def delete(self, episode_id: int):
        return self.repository.delete(episode_id)