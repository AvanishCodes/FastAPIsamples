from typing import Union
from pydantic import BaseModel
from fastapi import FastAPI, Response, status


app = FastAPI()


class Item(BaseModel):
    item_name: str


items = [
    {'item_name': 'Foo'},
    {'item_name': 'Bar'},
    {'item_name': 'Baz'},
]


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/items/")
async def read_item(skip: int = 0, limit: int = 10):
    return items[skip: skip + limit]


@app.post("/items/", status_code=status.HTTP_201_CREATED)
async def create_item(item: Item):
    items.append(item)
    return item
