"""Defaine all Users route endpoints here.



"""

from fastapi import APIRouter, Depends

from app.response import *
from .views import UserViews
from .schemas import *
from app.auth.router import auth_views


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
    current_user : UserModel = Depends(auth_views.get_current_active_user),
    limit : int = 10,
    page : int = 0
    ):
    return httpResponse(
        view_controll.get,
        res = res,
        limit = limit,
        page = page
        )