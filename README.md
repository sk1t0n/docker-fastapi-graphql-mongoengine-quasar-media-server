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

## GraphQL Query

    query {
        videos(skip: 0, limit: 3) {
            id
            title
            summary
            genres {
                id
                name
            }
            releaseDate
            runtime
        }
    }

    query {
        video(id: "5f6503a6b8a521f5c5071909") {
            id
            title
            genres {
                id
                name
            }
        }
    }

## GraphQL Mutation

    mutation {
        createVideo(
            title: "TEST8",
            summary: "SUMMARY",
            genres: [
                "5f5a6e7c49e4b08e7ae85c0f",
                "5f5f321b29b4cdad96b3cac2"
            ],
            releaseDate: "2020-09-18",
            runtime: 68
        ) {
            video {
                id
                title
                summary
                genres {
                    name
                }
            }
        }
    }

    mutation {
        deleteVideo(id: "5f6503dab8a521f5c507190a") {
            result
        }
    }
