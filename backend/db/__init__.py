import os

from dotenv import load_dotenv
from mongoengine import connect as conn

load_dotenv()
DB = os.getenv('MONGO_DB')
USER = os.getenv('MONGO_USER')
PASS = os.getenv('MONGO_PASSWORD')
IP = os.getenv('MONGO_IP', '127.0.0.1')
PORT = os.getenv('MONGO_PORT', 27017)


def connect():
    conn(host=f'mongodb://{USER}:{PASS}@{IP}:{PORT}/{DB}')
