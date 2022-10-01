from fastapi import FastAPI, HTTPException


app = FastAPI()


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


@app.get("/item/{item_id}")
async def read_item(item_id: int):
    if item_id > 0 and item_id >= len(items):
        raise HTTPException(status_code=404, detail="Item not found")
    return items[item_id]
