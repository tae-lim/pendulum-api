# https://github.com/tiangolo/uvicorn-gunicorn-fastapi-docker
# docker build -t pendulum_api ./
# docker run -d --name pendulum_api -p 80:80 pendulum_api
# docker run -d -p 80:80 -v $(pwd)/app:/app/app pendulum_api /start-reload.sh  # for development

FROM tiangolo/uvicorn-gunicorn-fastapi:python3.8

LABEL maintainer="Luis Cunha <lfcunha@gmail.com>"

COPY ./requirements.txt /app

RUN pip install -r /app/requirements.txt

COPY ./app /app/app