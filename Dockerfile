FROM python:3.9.18-alpine
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

RUN apk update \
    && apk add gcc musl-dev postgresql-dev python3-dev libffi-dev gettext


WORKDIR /app


# install dependencies
COPY . .
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt