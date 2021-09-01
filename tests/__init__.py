
from config import Config
Config.DB_URL = Config.DB_URL_TEST

from app import client

def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
