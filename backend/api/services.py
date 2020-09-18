from mongoengine import DoesNotExist, ValidationError
from mongoengine.queryset.queryset import QuerySet

from db import models


def get_video_list(skip: int, limit: int) -> QuerySet:
    return models.Video.objects.skip(skip).limit(limit).all()


def get_video_detail(id: str) -> models.Video:
    return models.Video.objects.get(id=id)


def create_video(**kwargs: dict) -> models.Video:
    return models.Video(**kwargs).save()


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


def create_genre(item):
    pass


def delete_genre(id: str):
    pass
