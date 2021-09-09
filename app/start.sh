#!/usr/bin/env sh

sleep 10

python manage.py migrate
python manage.py createsuperuser --noinput --username $DJANGO_SUPERUSER_ADMIN --email $DJANGO_SUPERUSER_EMAIL
if [ $TESTDATA -eq 1 ]; then python utils/autofill_db.py; else echo 'Test data flag not install, PASS'; fi
python manage.py runserver 0.0.0.0:8000