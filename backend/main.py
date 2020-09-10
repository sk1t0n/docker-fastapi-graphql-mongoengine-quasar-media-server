from fastapi import FastAPI

from db import connect, models

app = FastAPI()


@app.get('/')
async def root():
    connect()
    genre = models.Genre(name='Genre 1')
    result = genre.save()
    return {'result': result}
