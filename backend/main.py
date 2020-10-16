from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import graphene
from starlette.graphql import GraphQLApp

from db import connect, disconnect
from api.graphql import Query, Mutation


origins = [
    "http://localhost:8080",
    "http://127.0.0.1:8080",
    "http://localhost:8081",
    "http://127.0.0.1:8081"
]

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.on_event('startup')
def startup():
    connect()


@app.on_event('shutdown')
def shutdown():
    disconnect()


app.add_route(
    '/graphql',
    GraphQLApp(schema=graphene.Schema(query=Query, mutation=Mutation))
)
