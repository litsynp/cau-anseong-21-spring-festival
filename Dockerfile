# pull official base image
FROM python:3.8.3-alpine

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /web

# requirements.txt 파일 복사
COPY requirements.txt /web/

# 패키지 설치
RUN apk add libressl-dev libffi-dev gcc musl-dev gcc python3-dev musl-dev zlib-dev jpeg-dev #--(5.2)

# pip 설치 및 requirements 설치
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY . /web/
