from fastapi import APIRouter
from app.response import *
from .views import UserViews
from .schemas import *

user_router = APIRouter()
view_controll = UserViews()

@user_router.post("/", status_code = status.HTTP_201_CREATED, response_model = UserResponse)
async def addUser(
    res : Response,
    user : UserModel
    ):
    return httpResponse(
        view_controll.post,
        res = res,
        user = user
        )

@user_router.get("/", status_code = status.HTTP_200_OK, response_model = UsersResponse)
async def getUsers(
    res : Response,
    limit : int = 10,
    page : int = 0
    ):
    return httpResponse(
        view_controll.getUsers,
        res = res,
        limit = limit,
        page = page
        )