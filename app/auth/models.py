"""Authentication table will create here to store he users jwt token.

All transaction related to authorization must be defined here.

"""


from datetime import datetime, timedelta

from fastapi import Depends
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
import sqlalchemy as sql
from sqlalchemy.orm import relationship
from jose import JWTError, jwt

from database import Base, session
from app.Users.models import Users, EnumRole


SECRET_KEY = "70b56bafa6dd5f14ad1e17d994c7fc9f3ca4d6bab2ccd3c444d4fa684709f1b2"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 60


class AuthToken:
    
    token = ""
    user_id = ""
    expired_at : datetime = datetime.now

    def __init__(self,token, user_id, expired_at):
        self.token = token
        self.user_id = user_id
        self.expired_at = expired_at

    @staticmethod
    def create_token(data : dict):
        to_encode = data.copy()
        expired_at = datetime.now() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
        to_encode.update({"exp": expired_at})
        jwt_token = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
        return jwt_token, expired_at
    
    @staticmethod
    def add_new_token(user : Users):
        token, expired_at =AuthToken.create_token({"sub":user.email})
        auth_token = AuthToken(
                        token=token,
                        user_id=user.id,
                        expired_at= expired_at
                     )
        return auth_token
    
    @staticmethod
    def get_token_payload(token):
        return jwt.decode(token, SECRET_KEY, algorithms=ALGORITHM)