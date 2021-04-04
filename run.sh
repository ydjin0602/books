#!/bin/sh

export LISTEN_HOST="${LISTEN_HOST:=0.0.0.0}"
export LISTEN_PORT="${LISTEN_PORT:=8000}"
export WORKERS="${WORKERS:=5}"
export THREADS="${THREADS:=2}"

gunicorn --bind ${LISTEN_HOST}:${LISTEN_PORT} --workers ${WORKERS} --threads ${THREADS} app:app