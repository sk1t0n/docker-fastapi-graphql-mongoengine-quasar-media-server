# fastapi-quasar-media-server

FastAPI Media Server Implementation

## Run Media Server

1. Create a .env file in the "backend" folder with the following content:
    * MONGO_DB=\<database>
    * MONGO_USER=\<user>
    * MONGO_PASSWORD=\<password>
    * MONGO_IP=\<server-ip> (Optional)
    * MONGO_PORT=\<server-port> (Optional)
2. Create a requirements.txt file in the "backend" folder from Pipfile: `python3 -m pipenv lock -r > requirements.txt`
