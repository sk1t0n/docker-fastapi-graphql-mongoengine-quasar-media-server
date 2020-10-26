#! /usr/bin/env sh
set -e

HOST=${HOST:-0.0.0.0}
PORT=${PORT:-5000}
WORKERS=$(nproc)

# Generating a self-signed certificate using OpenSSL
# openssl req -x509 -out localhost.crt -keyout localhost.key \
# -newkey rsa:2048 -nodes -sha256 \
# -days 1825 \
# -subj '/CN=localhost' -extensions EXT -config <( \
# printf "[dn]\nCN=localhost\n[req]\ndistinguished_name = dn\n[EXT]\nsubjectAltName=DNS:localhost\nkeyUsage=digitalSignature\nextendedKeyUsage=serverAuth")

exec uvicorn main:app --reload \
    --host $HOST --port $PORT \
    --loop uvloop \
    --workers $WORKERS \
    --forwarded-allow-ips='*' \
    --proxy-headers \
    --ssl-certfile=./localhost.crt --ssl-keyfile=./localhost.key
