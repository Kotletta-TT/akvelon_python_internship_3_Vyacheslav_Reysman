#!/usr/bin/env sh

sleep 3

python manage.py migrate
python manage.py createsuperuser --noinput --username $DJANGO_SUPERUSER_ADMIN --email $DJANGO_DJANGO_SUPERUSER_EMAIL
python manage.py runserver 0.0.0.0:8000