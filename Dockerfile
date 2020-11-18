FROM python:3.8-alpine

RUN apk add --no-cache --virtual .build-deps gcc musl-dev

COPY requirements.txt /

RUN pip install -r /requirements.txt

COPY src/ /app
WORKDIR /app

CMD ["python", "/app/DiscordBot.py"]