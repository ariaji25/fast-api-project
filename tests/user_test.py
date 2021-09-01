from app.Users.models import Users
from fastapi import status
from requests.models import Response


from tests import client

# def test_user():
#     response = client.get("/api/v1/users")
#     print(response.json())
#     assert response.status_code == status.HTTP_200_OK

def test_user_login():
    # Users.initSuperAdmin()
    response : Response = client.post("/api/v1/auth/login", data={
        "username" : "ludes@gmail.com",
        "password" : "ludesadmin123"
    })
    print(response.content)
    assert response.status_code == status.HTTP_201_CREATED
    

# def test_post_user():
#     response = client.post(
#         "/users/", 
#         json={
#                 "name": "Abiabi",
#                 "email": "abiabi@mail.com",
#                 "password" : "mypassword",
#                 "bussines_name" : "abi cafe",
#                 "bussines_type" : "cafe"
#                 }
#         )
#     # print(response.json())
    
#     assert response.status_code == status.HTTP_201_CREATED