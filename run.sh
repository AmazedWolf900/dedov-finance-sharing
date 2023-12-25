#!/bin/sh
export FLASK_APP=app
export FLASK_ENV=development
sleep 5
python createdatabase.py
#flask run --debug --host=0.0.0.0 --port=8000
gunicorn -w 4 -b 0.0.0.0 'app:create_app()'