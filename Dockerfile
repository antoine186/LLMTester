# syntax=docker/dockerfile:1

FROM python:3.12.4-slim

WORKDIR /python-docker

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .

CMD [ "python", "-m" , "flask", "--app", "run:app", "run", "--host=0.0.0.0"]