from pydantic import BaseModel, ConfigDict


class ShowBase(BaseModel):
    title: str
    slug: str
    synopsis: str | None = None
    category: str | None = None
    section: str | None = None
    published: bool = False


class ShowCreate(ShowBase):
    pass


class ShowUpdate(BaseModel):
    title: str | None = None
    synopsis: str | None = None
    category: str | None = None
    section: str | None = None
    published: bool | None = None


class ShowResponse(ShowBase):
    id: int

    model_config = ConfigDict(from_attributes=True)