#! /usr/bin/env sh
celery -A worker.celery worker -l debug
