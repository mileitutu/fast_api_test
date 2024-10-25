from fastapi import FastAPI
import union


app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}