from typing import List, Optional
from datetime import datetime
from bson import ObjectId

from pydantic import BaseModel


class _VideoBase(BaseModel):
    _id: ObjectId
    title: str
    summary: Optional[str]
    runtime: int


class VideoList(_VideoBase):
    release_date: Optional[dict]
    genres: Optional[List[str]]


class VideoSingle(_VideoBase):
    release_date: Optional[dict]
    genres: Optional[List[dict]]


class VideoCreate(_VideoBase):
    release_date: Optional[datetime]
    genres: Optional[List[str]]


class VideoDelete(BaseModel):
    _id: ObjectId


class _GenreBase(BaseModel):
    _id: ObjectId
    name: str


class GenreList(_GenreBase):
    pass


class GenreSingle(_GenreBase):
    pass


class GenreCreate(_GenreBase):
    pass


class GenreDelete(_GenreBase):
    pass
