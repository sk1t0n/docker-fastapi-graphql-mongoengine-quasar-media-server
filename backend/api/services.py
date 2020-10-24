from mongoengine import DoesNotExist, ValidationError
from mongoengine.queryset.queryset import QuerySet

from db import models


def get_video_list(skip: int, limit: int) -> QuerySet:
    return models.Video.objects.skip(skip).limit(limit).all()


def get_video_count() -> int:
    return models.Video.objects.all().count()


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


def get_genre_list(skip: int, limit: int) -> QuerySet:
    return models.Genre.objects.skip(skip).limit(limit).all()


def get_genre_detail(id: str) -> models.Genre:
    return models.Genre.objects.get(id=id)


def create_genre(**kwargs: dict) -> models.Genre:
    return models.Genre(**kwargs).save()


def delete_genre(id: str) -> bool:
    try:
        models.Genre.objects.get(id=id).delete()
        return True
    except DoesNotExist:
        return False
    except ValidationError:
        return False
