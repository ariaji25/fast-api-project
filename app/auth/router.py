""" AUTH ROUTER.

Define all auth endpoint here like login, refresh token ec

"""

from fastapi import APIRouter

from .views import *
from app.response import *


auth_router = APIRouter()
auth_views = AuthViews()

@auth_router.post("/login", status_code = status.HTTP_201_CREATED, response_model = AuthResponse)
def login(
    res : Response,
    login_data : OAuth2PasswordRequestForm = Depends()
    ):
    return httpResponse(
        auth_views.post,
        res = res,
        login_data = login_data
    )