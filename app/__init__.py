from app.Users.models import Users
from fastapi import FastAPI, Response
from fastapi.security import OAuth2PasswordBearer
from fastapi.testclient import TestClient

app = FastAPI()

@app.get("/")
async def read_main():
    Users.initSuperAdmin()
    return "LUDES PBOB BE"

from .router import *

client = TestClient(app)