""" Schemas for users api endpoints response model.

Base on BaseModel from pydantic and typing

"""

from typing import List, Optional
from datetime import datetime

from pydantic.types import UUID4


from app.schemas import BaseModel, BaseResponse, ListMeta, Field

class UserModel(BaseModel):
    id : Optional[UUID4] = ""
    name : str = Field(min_length=3)
    email : str = Field(min_length=6) 
    password : str = Field(min_length=6)
    bussines_name : Optional[str] = ""
    bussines_type : Optional[str] = ""
    role : Optional[str] = ""
    is_active : Optional[bool] = False
    is_super : Optional[bool] = False
    is_verified: Optional[bool] = False
    created_at : Optional[datetime] = ""
    updated_at : Optional[datetime] = ""

    class Config:
        orm_mode = True

class UserResponse(BaseResponse):
    data : UserModel = None 


class UsersResponse(BaseResponse):
    data : List[UserModel] = []
    meta : ListMeta = ListMeta()