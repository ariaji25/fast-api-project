""" Auth views class defined for all auth endpoint action.
"""


from fastapi import APIRouter, status, HTTPException
from jose import jwt

from .models import AuthToken, Users, OAuth2PasswordBearer, OAuth2PasswordRequestForm, Depends
from .schemas import *
from .auth_extentions import get_current_user
from app.Users.models import EnumRole


class AuthViews:

    """ View controll for authorization endpoint,
    """

    unauthorize_excepion = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED, detail="You dont allowed to this function")
    in_active_exception = HTTPException(
        status_code=status.HTTP_404_NOT_FOUND, detail="Inactive User")

    def __init__(self):
        pass

    def post(self, login_data: OAuth2PasswordRequestForm):
        auth_response = AuthResponse()
        auth_response.notfound()
        user: Users = Users.exist(Users.email == login_data.username)
        if not user:
            auth_response.message = "user wit username not found"
            return auth_response
        if not user.verify_password(login_data.password):
            auth_response.message = "password incorrect"
            auth_response.badrequest
            return auth_response
        auth_token: AuthToken = AuthToken.add_new_token(user)
        auth_response.data = AuthTokenModel(
            token=auth_token.token,
            expired_at=auth_token.expired_at,
            user_id=auth_token.user_id
        )
        auth_response.created()
        return auth_response

    def get_current_active_user(self, current_user: UserModel = Depends(get_current_user)):
        if current_user.is_active:
            return current_user
        else:
            raise self.in_active_exception

    def get_current_active_admin(self, current_admin: UserModel = Depends(get_current_user)):
        if current_admin.is_active and current_admin.role == EnumRole.ADMIN:
            return current_admin
        raise self.unauthorize_excepion

    def get_current_active_super_admin(self, current_admin: UserModel = Depends(get_current_user)):
        if current_admin.is_active and current_admin.role == EnumRole.SUPER_ADMIN:
            return current_admin
        raise self.unauthorize_excepion

    def get_current_mercent_admin(self, current_mercent_admin: UserModel = Depends(get_current_user)):
        if current_mercent_admin.is_active and current_mercent_admin.role == EnumRole.MERCENT_ADMIN or current_mercent_admin.role == EnumRole.ADMIN:
            raise self.unauthorize_excepion
        return current_mercent_admin
