from typing import Union
from pydantic import BaseModel
from fastapi import FastAPI, status, HTTPException


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


@app.get("/items/{item_id}")
async def read_item(item_id: int):
    if (item_id < 0) or (item_id > 0 and item_id >= len(items)):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Item not found")
    return items[item_id]


@app.post("/items/", status_code=status.HTTP_201_CREATED)
async def create_item(item: Item):
    items.append(item)
    return item


@app.delete("/items/{item_id}")
async def delete_item(item_id: int):
    if (item_id < 0) or (item_id > 0 and item_id >= len(items)):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Item not found")
    items.pop(item_id)
    return {"item_id": item_id}
