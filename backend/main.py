from fastapi import FastAPI

from db import connect

app = FastAPI()


@app.get('/')
async def root():
    connect()
    return {'message': 'TEST'}
