from sqlalchemy import (
    Column,
    Integer,
    String,
    Boolean,
    ForeignKey
)

from sqlalchemy.orm import relationship

from app.db.base import Base


class Episode(Base):
    __tablename__ = "episodes"

    id = Column(Integer, primary_key=True, index=True)

    season_id = Column(
        Integer,
        ForeignKey("seasons.id"),
        nullable=False
    )

    episode_number = Column(Integer, nullable=False)

    title = Column(String(255), nullable=False)

    duration_seconds = Column(Integer)

    language = Column(String(20))

    content_group = Column(String(255))

    artwork = Column(Boolean, default=False)

    published = Column(Boolean, default=False)

    season = relationship(
        "Season",
        back_populates="episodes"
    )
    