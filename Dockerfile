# docker build -t pendulum_api ./
# docker run -d --name pendulum_api -p 80:80 pendulum_api

FROM tiangolo/uvicorn-gunicorn-fastapi:python3.8

LABEL maintainer="Luis Cunha <lfcunha@gmail.com>"

COPY ./requirements.txt /app

RUN pip install -r /app/requirements.txt

COPY ./app /app/app