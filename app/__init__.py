from fastapi import FastAPI, Response
from fastapi.testclient import TestClient

app = FastAPI()


@app.get("/")
async def read_main():
    return {"msg": "Hello World"}

from .router import *

client = TestClient(app)