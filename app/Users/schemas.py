from app.schemas import BaseModel, BaseResponse, ListMeta, Field
from typing import List, Optional

class UserModel(BaseModel):
    id : Optional[int] = Field(description="user id, generate from server")
    name : str = Field(min_length=5, description="user's full name")
    email : str = Field(min_length=10, description="user's email")

class UserResponse(BaseResponse):
    data : UserModel = None 


class UsersResponse(BaseResponse):
    data : List[UserModel] = []
    meta : ListMeta = ListMeta()