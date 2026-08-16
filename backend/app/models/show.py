from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.orm import relationship

from app.db.base import Base


class Show(Base):
    __tablename__ = "shows"

    id = Column(Integer, primary_key=True, index=True)

    title = Column(String(255), nullable=False)

    slug = Column(String(255), unique=True, nullable=False)

    synopsis = Column(String)

    category = Column(String)

    section = Column(String)

    published = Column(Boolean, default=False)

    seasons = relationship(
        "Season",
        back_populates="show",
        cascade="all, delete-orphan"
    )

