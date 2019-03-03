#!/bin/sh

python manager.py db migrate
python manager.py db upgrade
gunicorn --bind=0.0.0.0:8000 --log-level info --workers 4 twittor.wsgi:application
