from .models import Users
from .schemas import UserModel, UserResponse, UsersResponse, ListMeta

class UserViews:

    def post(self, user : UserModel):
        response = UserResponse()
        response.badrequest()
        user = Users.addUser(user)
        if user is None:
            response.message = "user is exist"
            return response
        response = UserResponse(data=user.toModel())
        response.created()
        return response
    
    def getUsers(self, limit, page):
        response = UsersResponse()
        users = Users.getUsers(limit, page)
        users = [u.toModel() for u in users]
        response.data = users
        response.meta.totals = len(users)
        response.meta.limit = limit
        response.meta.curent_page = page
        response.meta.next_page = page + 1
        response.meta.previous_page = page -1
        return response