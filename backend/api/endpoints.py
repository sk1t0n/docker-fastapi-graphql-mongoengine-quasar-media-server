from typing import List

from fastapi import APIRouter, Response

from db import schemas
from . import services

router = APIRouter()


@router.get('/videos', response_model=List[schemas.VideoList])
async def get_video_list(skip: int = 0, limit: int = 5):
    return services.get_video_list(skip, limit)


@router.get('/videos/{id}', response_model=schemas.VideoSingle)
async def get_video_detail(id: str):
    result = services.get_video_detail(id)
    if result:
        return result
    return Response(status_code=404)


@router.post('/videos', response_model=schemas.VideoCreate)
async def create_video(item: schemas.VideoCreate):
    result = services.create_video(item)
    if result:
        return Response(status_code=201)
    return None


@router.delete('/videos/{id}', response_model=schemas.VideoDelete)
async def delete_video(id: str):
    result = services.delete_video(id)
    if result:
        return Response(status_code=200)
    else:
        return Response(status_code=404)


@router.get('/genres', response_model=List[schemas.GenreList])
async def get_genre_list(skip: int = 0, limit: int = 2):
    pass


@router.get('/genres/{id}', response_model=schemas.GenreSingle)
async def get_genre_detail(id: str):
    pass


@router.post('/genres', response_model=schemas.GenreCreate)
async def create_genre(item: schemas.GenreCreate):
    pass


@router.delete('/genres/{id}', response_model=schemas.GenreDelete)
async def delete_genre(id: str):
    pass
