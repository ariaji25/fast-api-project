from fastapi import status

from tests import client

def test_user():
    response = client.get("/users")
    print(response.json())
    assert response.status_code == status.HTTP_200_OK

def test_post_user():
    response = client.post(
        "/users/", 
        json={
                "name": "Abiabi",
                "email": "abiabi@mail.com",
                "password" : "mypassword",
                "bussines_name" : "abi cafe",
                "bussines_type" : "cafe"
                }
        )
    # print(response.json())
    
    assert response.status_code == status.HTTP_201_CREATED