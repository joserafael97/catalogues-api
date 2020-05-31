#!/usr/bin/env bash
# wait for Postgres to start
sleep 20

python manage.py migrate
python manage.py runserver 0.0.0.0:8000 --settings=catalogues.settings.production