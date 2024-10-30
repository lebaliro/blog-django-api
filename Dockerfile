FROM python:3.11

RUN pip install -U pip setuptools
RUN pip install poetry

WORKDIR /app
COPY . .

RUN poetry install
