FROM python:3.9-slim-buster

WORKDIR /app

COPY src/ .
COPY .env .

RUN pip install --no-cache-dir Faker

CMD ["python", "main.py"]