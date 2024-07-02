# syntax=docker/dockerfile:1

FROM python:3.12.4-slim

WORKDIR /python-docker

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .

RUN apt-get -y update; apt-get -y install curl

RUN curl -fsSL https://ollama.com/install.sh | sh

CMD ollama serve & \
    sleep 5 && \
    ollama pull llama3 && \
    ollama run llama3 & \
    python -m flask --app run:app run --host=0.0.0.0