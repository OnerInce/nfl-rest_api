FROM python:3.8

ENV PYTHONBUFFERED 1

COPY docker-entrypoint.sh /usr/local/bin/docker-entrypoint.sh

RUN mkdir /code
WORKDIR /code
COPY . /code/

RUN chmod 755 /usr/local/bin/docker-entrypoint.sh
ENTRYPOINT ["/usr/local/bin/docker-entrypoint.sh"]

RUN pip install -r requirements.txt
