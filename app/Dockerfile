FROM python:3.8.1-alpine3.11

ARG APP_DIR=/var/app

RUN mkdir $APP_DIR

ADD ./requirements.txt $APP_DIR

WORKDIR $APP_DIR

RUN \
    apk add --no-cache --virtual .build-deps gcc g++ musl-dev make linux-headers && \
    apk add --no-cache libressl-dev musl-dev libffi-dev && \
    python3 -m pip install -r requirements.txt --no-cache-dir && \
    apk --purge del .build-deps

RUN pip install -r requirements.txt
