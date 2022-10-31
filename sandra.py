from fastapi import FastAPI
import uvicorn
import os

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}

if __name__ == "__main__":
    uvicorn.run("sandra:app", host="0.0.0.0", port=int(os.environ.get('PORT', 8002)), log_level="info")