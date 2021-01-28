from fastapi import APIRouter


from typing import Optional, List, Any
import asyncio
import json
import sys
sys.path.append("/app/")
from app.utils import JSONEncoder

from fastapi import FastAPI, Query
import motor.motor_asyncio
import uvloop

from app.database import aggregate_features
from app.config import DB
from app.controllers import *

from app.utils import get_secret

mongdb_config = get_secret("mongodb_atlas_admin")


mongo_connection_string = f"mongodb+srv://{mongdb_config.get('username')}:{mongdb_config.get('password')}@{mongdb_config.get('host')}/{DB}?retryWrites=true&w=majority"
client = motor.motor_asyncio.AsyncIOMotorClient(mongo_connection_string)
database = "products"

db = client[database]
collection = db["handbags"]

router = APIRouter()


async def get_one():
    result = await collection.find_one()
    return result


async def do_insert():
    r = await do_insert()
    return r


@router.get("/")
async def read_root():
    r1 = await get_one()
    return {"Hello": json.dumps(r1, cls=JSONEncoder)}


@router.get("/items/{item_id}")
async def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id+1, "q": q}


@router.get("/dashboard")
async def dashboard(start_date: Optional[int] = Query(20200101, ge=20200101, le=20301231),
                    end_date: Optional[int] = Query(20200102, ge=20200101, le=20301231),
                    brands: Optional[List] = None,
                    vendors: Optional[List] = None):
    user_id = 1  # TODO: get userid from middleware (receive it in jwt token headers)
    user = User(user_id)
    controller = Dashboard(user, start_date, end_date, brands, vendors)

    # TODO need middleware to turn the response into json?
    return controller.get_dashboard_data(collection)
