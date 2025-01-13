FROM python:3.9.7-slim-buster

WORKDIR .
COPY . .


CMD gunicorn app:app & python3 main.py
