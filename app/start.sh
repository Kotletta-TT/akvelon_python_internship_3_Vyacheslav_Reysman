#!/usr/bin/env sh

sleep 10

python manage.py migrate
python manage.py createsuperuser --noinput --username $DJANGO_SUPERUSER_ADMIN --email $DJANGO_SUPERUSER_EMAIL
if [ -z "$TESTDATA" ]; then echo 'Test data flag not install, PASS'; else python app/utils/autofill_db.py; fi
python manage.py runserver 0.0.0.0:8000