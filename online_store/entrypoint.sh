#!/bin/bash

python3 manage.py migrate

gunicorn core.wsgi:application -b 0.0.0.0:8000