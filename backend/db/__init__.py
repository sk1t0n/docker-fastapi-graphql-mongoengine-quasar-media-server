import os

from dotenv import load_dotenv
from mongoengine import connect as _connect, disconnect as _disconnect

container_env_path = os.path.dirname(
        os.path.dirname(os.path.abspath(__file__))
    ) + '/.env'
load_dotenv(dotenv_path=container_env_path)
DB = os.getenv('MONGO_DB')
USER = os.getenv('MONGO_USER')
PASS = os.getenv('MONGO_PASSWORD')
IP = os.getenv('MONGO_IP', '172.30.0.3')
PORT = os.getenv('MONGO_PORT', 27017)


def connect():
    _connect(host=f'mongodb://{USER}:{PASS}@{IP}:{PORT}/{DB}')


def disconnect():
    _disconnect()
