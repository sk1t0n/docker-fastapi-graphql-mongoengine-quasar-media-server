#! /usr/bin/env sh
set -e

HOST=${HOST:-0.0.0.0}
PORT=${PORT:-5000}
WORKERS=$(nproc)

exec uvicorn main:app --reload \
    --host $HOST --port $PORT \
    --loop uvloop \
    --workers $WORKERS
