from pydantic import BaseModel, Field
from fastapi import status

class BaseResponse(BaseModel):
    message : str = "OK"
    filed : bool = False
    status_code : int = status.HTTP_200_OK
    
    def error(self):
        self.filed = True

    def success(self):
        self.filed = False
    
    def created(self):
        self.success()
        self.message = "success created data"
        self.status_code = status.HTTP_201_CREATED
    
    def notfound(self):
        self.error()
        self.message = "data not found"
        self.status_code = status.HTTP_404_NOT_FOUND
    
    def badrequest(self):
        self.error()
        self.message = "bad request"
        self.status_code = status.HTTP_400_BAD_REQUEST
        

class ListMeta(BaseModel):
    totals : int = 0
    next_page : int = 0
    curent_page : int = 0
    previous_page : int = 0
    limit : int =0
    