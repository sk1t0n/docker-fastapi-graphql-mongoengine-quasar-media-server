FROM python:3.8-slim

LABEL maintainer="Anton Grabovsky <skiton25@gmail.com>"

WORKDIR /app
COPY . /app

RUN pip install -U pip && pip install --no-cache-dir -r requirements.txt

ENV HOST=0.0.0.0
ENV PORT=5000

EXPOSE $PORT

RUN groupadd -r fastapi && \
    useradd --no-log-init -r -g fastapi fastapi && \
    chown -R fastapi:fastapi /app
USER fastapi

ENTRYPOINT ["sh", "/app/start.sh"]
