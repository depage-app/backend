FROM python:3.8-slim-buster

WORKDIR ./

COPY requirements.txt requirements.txt

RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt

COPY . .


CMD uvicorn main:app --host ${APP_HOST} --port ${APP_PORT}