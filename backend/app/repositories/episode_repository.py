from sqlalchemy.orm import Session

from app.models.episode import Episode
from app.schemas.episode import EpisodeCreate, EpisodeUpdate


class EpisodeRepository:
    def __init__(self, db: Session):
        self.db = db

    def get_all(self):
        return self.db.query(Episode).all()

    def get_by_id(self, episode_id: int):
        return (
            self.db.query(Episode)
            .filter(Episode.id == episode_id)
            .first()
        )

    def create(self, episode: EpisodeCreate):
        db_episode = Episode(**episode.model_dump())

        self.db.add(db_episode)
        self.db.commit()
        self.db.refresh(db_episode)

        return db_episode

    def update(self, episode_id: int, episode: EpisodeUpdate):
        db_episode = self.get_by_id(episode_id)

        if not db_episode:
            return None

        update_data = episode.model_dump(exclude_unset=True)

        for key, value in update_data.items():
            setattr(db_episode, key, value)

        self.db.commit()
        self.db.refresh(db_episode)

        return db_episode

    def delete(self, episode_id: int):
        db_episode = self.get_by_id(episode_id)

        if not db_episode:
            return None

        self.db.delete(db_episode)
        self.db.commit()

        return db_episode