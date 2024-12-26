
from fastapi import APIRouter, status, Response
from pydantic import BaseModel
import os 
from dataclasses import dataclass, field

if os.environ.get("ENABLE_DB"):
    from ..shared.database import db
    

router = APIRouter()

router_name = "item"

class Database:

    def __init__(self) -> None:
        if os.environ.get("ENABLE_DB"):
            self.collection = db.get_collection("item")

    async def create(self):
        if os.environ.get("ENABLE_DB"):
            result = self.collection.insert_one({})
        else:
            return {}

    async def get(self):
        if os.environ.get("ENABLE_DB"):
            result = self.collection.insert_one({})
        else:
            return {} 

    async def list(self):
        if os.environ.get("ENABLE_DB"):
            result = self.collection.insert_one({})
        else:
            return {} 

    async def update(self):
        if os.environ.get("ENABLE_DB"):
            result = self.collection.insert_one({})
        else:
            return {} 

    async def delete(self):
        if os.environ.get("ENABLE_DB"):
            result = self.collection.insert_one({})
        else:
            return {} 




class Model(BaseModel):
    id : str 



@router.post(f"/", status_code=status.HTTP_201_CREATED)
async def create(response : Response):
    return {}



@router.get("/{id}/", status_code=status.HTTP_200_OK)
async def get(id : int, response : Response):
    return {}


@router.get(f"/", status_code=status.HTTP_200_OK)
async def list(response : Response):
    return {}


@router.put("/{id}/", status_code=status.HTTP_200_OK)
async def update(id : int, response : Response):
    return {}


@router.delete("/{id}/", status_code=status.HTTP_200_OK)
async def delete(id : int, response : Response):
    return {}