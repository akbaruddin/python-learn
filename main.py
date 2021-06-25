from fastapi import FastAPI
from pydantic import BaseModel

import uvicorn

app = FastAPI()


@app.get("/")
def read_root():
    return {"hello": "world"}


# Path Parameters
@app.get("/course/{course_id}")
def my_course(course_id: int):
    return {"course_id": course_id}


dummy_data = [i for i in range(100)]


# Query Parameters
@app.get("/reads/")
def read_items(page: int = 0, limit: int = 0, skip: int = 1):
    return dummy_data[page * 10: page * 10 + limit: skip]


# Base Model
class WriteItem(BaseModel):
    name: str
    info: str = None
    price: float
    qty: int


@app.post("/write-item/")
async def create_item(item: WriteItem):
    return {"amount": item.qty * 100, "success": True}


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=5000, log_level="info")
