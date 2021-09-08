FROM python:3.9

WORKDIR /usr/src/app

COPY app/ .

RUN pip install --no-cache-dir pipenv && pipenv lock && pipenv install --system --deploy --clear