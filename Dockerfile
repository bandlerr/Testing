FROM python:3.9.6-buster

COPY . /app

WORKDIR /app

CMD ["python", "tests/test.py"]