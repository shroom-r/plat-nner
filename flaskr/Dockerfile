FROM python:3.10-alpine AS builder

WORKDIR /code
COPY requirements.txt /code
RUN --mount=type=cache,target=/root/.cache/pip \
  pip3 install -r requirements.txt

COPY . .

ARG FLASK_ENV
ARG FLASK_DEBUG

ENV FLASK_APP app/
ENV FLASK_ENV $FLASK_ENV
ENV FLASK_DEBUG $FLASK_DEBUG
ENV FLASK_RUN_PORT 8000
ENV FLASK_RUN_HOST 0.0.0.0

EXPOSE 8000

CMD flask db upgrade && gunicorn --config ./app/gunicorn_config.py "app:create_app()"