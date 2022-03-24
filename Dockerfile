FROM python:3.10-slim-bullseye

RUN mkdir -p /app/dr-trainer

COPY . /app/dr-trainer

WORKDIR /app/dr-trainer

RUN pip install -r src/requirements.txt

EXPOSE 3033

CMD uvicorn src.main:app --host 0.0.0.0 --port 3033
