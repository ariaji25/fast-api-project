from test import client
from fastapi import status

def test_user():
    response = client.get("/users")
    print(response.json())
    assert response.status_code == status.HTTP_200_OK

def test_post_user():
    response = client.post(
        "/users/", 
        json={
                "name": "Abiabi",
                "email": "abiabi@mail.com"
                }
        )
    # print(response.json())
    
    assert response.status_code == status.HTTP_201_CREATED