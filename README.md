# pendulum-api
Backend API for the single page react user website


### Run fastapi server:
 1) run directly:
    ```bash
    uvicorn main:app --reload
    ```
 2) or with **Docker** 
    - development env:
         - link local development directory
         - use hot-reload script
    ```bash
    docker run -d -p 80:80 -v $(pwd)/app:/app/app pendulum_api /start-reload.sh
    ```
    - production env:
    ```bash
    docker run -d --name pendulum_api -p 80:80 pendulum_api
    ```
   
 - see [here](https://github.com/tiangolo/uvicorn-gunicorn-fastapi-docker) for additional options, including
 running with gunicorn
 - There's a script to run things prior to start the server, e.g. alembic migrations
 