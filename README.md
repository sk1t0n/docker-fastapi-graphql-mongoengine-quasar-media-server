# fastapi-quasar-media-server

FastAPI Media Server Implementation

## Run Media Server

1. Create a .env file in root folder with the following content:
    * MONGO_INITDB_ROOT_USERNAME=\<root_username>
    * MONGO_INITDB_ROOT_PASSWORD=\<root_password>
    * MONGO_INITDB_DATABASE=\<database_name>
2. Create a .env file in the "backend" folder with the following content:
    * MONGO_DB=\<MONGO_INITDB_DATABASE from  .env file in root folder>
    * MONGO_USER=\<username>
    * MONGO_PASSWORD=\<password>
3. Change values in /db/init.js:
    * user: "\<MONGO_USER from /backend/.env>"
    * pwd: "\<MONGO_PASSWORD from /backend/.env>"
    * db: "\<MONGO_DB from /backend/.env>"
4. Create a requirements.txt file in the "backend" folder from Pipfile: `python3 -m pipenv lock -r > requirements.txt`
