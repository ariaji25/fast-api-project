""" All response models for auth endpoint must defined here.
"""

from typing import List, Optional
from datetime import datetime

from app.schemas import BaseModel, BaseResponse
from app.Users.schemas import UserModel


class AuthTokenModel(BaseModel):
    token : str 
    expired_at : datetime
    user : UserModel

    class Config:
        orm_mode = True

class AuthResponse(BaseResponse):
    data : AuthTokenModel = None

class TokenData(BaseModel):
    username : str