""" Main Api Router.

Import All defined router here, in include it to app router.

"""

from app.Users.router import user_router
from app import app
from app.auth.router import auth_router

ROOT_PATH = "/api/v1"
app.include_router(user_router, prefix="{}/users".format(ROOT_PATH))
app.include_router(auth_router, prefix="{}/auth".format(ROOT_PATH))
