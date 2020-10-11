from app.Users.router import user_router
from app import app

app.include_router(user_router, prefix="/users")