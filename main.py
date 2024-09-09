from typing import Union
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    name: str
    price: float

@app.get("/hello")
def read_root():
    return {"message": "Hello Worldss"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

@app.post("/items")
def insert_item( item: Item):
    return {'body':item}

@app.put("/items/{item_id}")
def update_item(item_id: int, updated_item: Item):
    return {"item_id": item_id, "item": updated_item}
