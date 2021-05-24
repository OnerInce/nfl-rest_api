FROM python:latest

ENV PYTHONBUFFERED 1

RUN mkdir /code
WORKDIR /code
COPY . /code/

RUN pip install -r requirements.txt
