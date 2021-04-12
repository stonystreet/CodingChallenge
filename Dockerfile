FROM python:alpine3.7

RUN mkdir /logs
COPY ./server.py /app/
WORKDIR /app

ENTRYPOINT ["python", "server.py"]

