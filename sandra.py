from fastapi import FastAPI
import uvicorn
import os

fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/items/{item_id}")
async def read_item(item_id):
    return {"item_id": item_id}

@app.get("/items/")
async def read_item(skip: int = 0, limit: int = 10):
    return fake_items_db[skip : skip + limit]

if __name__ == "__main__":
    uvicorn.run("sandra:app", host="0.0.0.0", port=int(os.environ.get('PORT', 8002)), log_level="info")