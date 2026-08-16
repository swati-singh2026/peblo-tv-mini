from pydantic import BaseModel, ConfigDict


class SeasonBase(BaseModel):
    show_id: int
    season_number: int
    title: str


class SeasonCreate(SeasonBase):
    pass


class SeasonUpdate(BaseModel):
    title: str | None = None


class SeasonResponse(SeasonBase):
    id: int

    model_config = ConfigDict(from_attributes=True)