# syntax=docker/dockerfile:1

FROM python:3.8-slim-buster

WORKDIR /compare

COPY . .

CMD ["python","main.py"]
