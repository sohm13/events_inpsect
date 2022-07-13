FROM python:3.9-slim-buster

RUN useradd --create-home var \
    && apt-get update \
    && apt-get install -y --no-install-recommends build-essential libffi-dev libpq-dev gcc procps \
    && pip install -r requirements.txt \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app
COPY . .

CMD ["run", "python", "main.py"]