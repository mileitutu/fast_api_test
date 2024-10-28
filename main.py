from fastapi import FastAPI
from typing import Optional  # 使用 Optional 来改善可读性
from pydantic import BaseModel

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):  # 使用 Optional 更清晰
    return {"item_id": item_id, "q": q}
