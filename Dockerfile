FROM python:3.8

WORKDIR /root/qover
COPY . .
RUN pip install poetry
RUN poetry install --no-root
CMD ["poetry", "run", "python", "app.py", "--run_demo", "--port=9090", "--worker=100"]
EXPOSE 9090
