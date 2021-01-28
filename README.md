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
    
    First build the image:
    ```bash
    docker build -t pendulum_api:0.01 ./
    ```
    Then run the container:
    ```bash
    docker run --name pendulum_api -it -p 80:80 -v $(pwd)/app:/app/app -v ~/.aws/:/root/.aws:ro pendulum_api:0.0.1 /start-reload.sh
    ```
    - production env:
    ```bash
    docker run -d --name pendulum_api -p 80:80 pendulum_api
    ```
   
 - see [here](https://github.com/tiangolo/uvicorn-gunicorn-fastapi-docker) for additional options, including
 running with gunicorn
 - There's a script to run things prior to start the server, e.g. alembic migrations
 