#!/bin/sh

export LISTEN_HOST="${LISTEN_HOST:=0.0.0.0}"
export WORKERS="${WORKERS:=5}"
export THREADS="${THREADS:=2}"

gunicorn --bind ${LISTEN_HOST}:8000 --workers ${WORKERS} --threads ${THREADS} app:app