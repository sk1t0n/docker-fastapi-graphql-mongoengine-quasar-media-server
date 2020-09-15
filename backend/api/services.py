import json
from typing import Optional

from mongoengine import DoesNotExist, ValidationError

from db import models, schemas


def get_video_list(skip: int, limit: int) -> Optional[dict]:
    video_list = models.Video.objects.skip(skip).limit(limit).all()
    data = json.loads(video_list.to_json())
    return data


def get_video_detail(id: str) -> Optional[dict]:
    try:
        video = models.Video.objects.get(id=id)
        data = json.loads(video.to_json())
        return data
    except DoesNotExist:
        return None
    except ValidationError:
        return None


def create_video(item: schemas.VideoCreate) -> Optional[dict]:
    new_video = models.Video(**item.dict()).save()
    data = json.loads(new_video.to_json())
    return data


def delete_video(id: str) -> bool:
    try:
        models.Video.objects.get(id=id).delete()
        return True
    except DoesNotExist:
        return False
    except ValidationError:
        return False


def get_genre_list(skip: int = 0, limit: int = 2):
    pass


def get_genre_detail(id: str):
    pass


def create_genre(item: schemas.GenreCreate):
    pass


def delete_genre(id: str):
    pass
