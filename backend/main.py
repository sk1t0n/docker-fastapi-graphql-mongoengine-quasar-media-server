from fastapi import FastAPI

from db import connect, disconnect
from api.endpoints import router

app = FastAPI(
    openapi_url='/api/v1/openapi.json',
    docs_url='/api/v1/docs',
    redoc_url='/api/v1/redoc'
)


@app.on_event('startup')
def startup():
    connect()


@app.on_event('shutdown')
def shutdown():
    disconnect()


app.include_router(router, prefix='/api/v1')
