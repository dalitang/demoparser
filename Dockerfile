FROM python:3.8-slim

ADD ./requirements/dev.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

WORKDIR /app
