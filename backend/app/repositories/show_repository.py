from sqlalchemy.orm import Session

from app.models.show import Show
from app.schemas.show import ShowCreate, ShowUpdate


class ShowRepository:

    def __init__(self, db: Session):
        self.db = db

    def get_all(self):
        return self.db.query(Show).all()

    def get_by_id(self, show_id: int):
        return (
            self.db.query(Show)
            .filter(Show.id == show_id)
            .first()
        )

    def create(self, show_data: ShowCreate):
        show = Show(
            title=show_data.title,
            slug=show_data.slug,
            synopsis=show_data.synopsis,
            category=show_data.category,
            section=show_data.section,
            published=show_data.published,
        )

        self.db.add(show)
        self.db.commit()
        self.db.refresh(show)

        return show

    def update(self, show_id: int, show_data: ShowUpdate):

        show = self.get_by_id(show_id)

        if not show:
            return None

        update_data = show_data.model_dump(exclude_unset=True)

        for key, value in update_data.items():
            setattr(show, key, value)

        self.db.commit()
        self.db.refresh(show)

        return show

    def delete(self, show_id: int):

        show = self.get_by_id(show_id)

        if not show:
            return False

        self.db.delete(show)
        self.db.commit()

        return True
    