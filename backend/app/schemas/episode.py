from pydantic import BaseModel, ConfigDict


class EpisodeBase(BaseModel):
    season_id: int
    episode_number: int
    title: str
    duration_seconds: int | None = None
    language: str | None = None
    content_group: str | None = None
    artwork: bool = False
    published: bool = False


class EpisodeCreate(EpisodeBase):
    pass


class EpisodeUpdate(BaseModel):
    title: str | None = None
    duration_seconds: int | None = None
    language: str | None = None
    content_group: str | None = None
    artwork: bool | None = None
    published: bool | None = None


class EpisodeResponse(EpisodeBase):
    id: int

    model_config = ConfigDict(from_attributes=True)