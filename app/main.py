import asyncio
import sys
sys.path.append("/app/")

from fastapi import FastAPI
import uvloop

from app.routers import v1


app = FastAPI()

app.include_router(
    v1.router,
    prefix="/v1"
)

asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())
loop = asyncio.get_event_loop()
