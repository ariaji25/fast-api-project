""" All response models for auth endpoint must defined here.
"""

from typing import List, Optional
from datetime import datetime
from uuid import UUID

from app.schemas import BaseModel, BaseResponse
from app.Users.schemas import UserModel


class AuthTokenModel(BaseModel):
    token : str 
    expired_at : datetime
    user_id : UUID

    class Config:
        orm_mode = True

class AuthResponse(BaseResponse):
    data : AuthTokenModel = None

class TokenData(BaseModel):
    username : str