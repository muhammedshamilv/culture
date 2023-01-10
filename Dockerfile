FROM python:3.10.6-alpine3.16
RUN apk add git build-base linux-headers libffi-dev
WORKDIR /backend
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY . .
