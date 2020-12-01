from typing import Optional, List, Any
import asyncio
import json

from bson import ObjectId
from fastapi import FastAPI, Query
import motor.motor_asyncio
import uvloop

from app.database import aggregate_features
from app.controllers import *


class JSONEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, ObjectId):
            return str(o)
        return json.JSONEncoder.default(self, o)


app = FastAPI()

mongo_connection_string = "mongodb+srv://admin:LkUuo73ELzqW*GPG@cluster0.dfbrs.mongodb.net/products?retryWrites=true&w=majority"
client = motor.motor_asyncio.AsyncIOMotorClient(mongo_connection_string)
database = "products"

db = client[database]
collection = db["handbags"]

asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())
loop = asyncio.get_event_loop()


async def do_insert():
    result = await collection.find_one()
    return result


async def get_one():
    r = await do_insert()
    return r


@app.get("/")
async def read_root():
    r1 = await get_one()
    return {"Hello": json.dumps(r1, cls=JSONEncoder)}


@app.get("/items/{item_id}")
async def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}


@app.get("/dashboard")
async def dashboard(start_date: Optional[int] = Query(20200101, ge=20200101, le=20301231),
                    end_date: Optional[int] = Query(20200102, ge=20200101, le=20301231),
                    brands: Optional[List] = None,
                    vendors: Optional[List] = None
                    ):
    user_id = 1  # TODO get userid from middleware (send it in jwt token headers)
    user = User(user_id)
    controller = Dashboard(user, start_date, end_date, brands, vendors)

    # TODO need middleware to turn the response into json
    return controller.get_dashboard_data(collection)

