FROM python:3.8.5

WORKDIR /usr/src/app

COPY ./bot/requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

COPY ./bot/ .

