"""Users view controol to serilize the users response endpoint to BaseResponse model.

All transaction from user router endpoint must request to this class.

"""


from .models import Users
from .schemas import UserModel, UserResponse, UsersResponse, ListMeta

class UserViews:

    def post(self, user : UserModel):
        response = UserResponse()
        response.badrequest()
        user = Users.addUser(user)
        if user is None:
            response.message = "email is has been used"
            return response
        response.data = user
        response.created()
        return response
    
    def get(self, limit, page):
        response = UsersResponse()
        response.data = Users.getUsers(limit, page)
        print(response.data)
        response.meta.totals = len(response.data)
        response.meta.limit = limit
        response.meta.curent_page = page
        response.meta.next_page = page + 1
        response.meta.previous_page = page -1
        return response