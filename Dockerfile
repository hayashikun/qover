FROM python:3.8

WORKDIR /root/qover
COPY . .
RUN pip install poetry
RUN poetry install --no-root
