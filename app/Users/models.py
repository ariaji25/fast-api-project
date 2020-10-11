from database import Base, session
from sqlalchemy import *
from .schemas import UserModel
from datetime import datetime


class Users(Base):

    __tablename__ = "users"
    
    id = Column(Integer,primary_key=True, index=True)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False, unique=True, index=True)
    timestamp = Column(DateTime, default=datetime.now())

    @staticmethod
    def exist(*args, **kwargs):
        return session.query(Users).filter(*args, **kwargs).first()

    @staticmethod
    def fromModel(user : UserModel):
        return Users(
            name=user.name,
            email=user.email
        )
    
    def toModel(self):
        return UserModel(
            id=self.id,
            name=self.name,
            email=self.email,
        )
    
    @staticmethod
    def addUser(user : UserModel):
        user_exist = Users.exist(Users.email==user.email)
        if user_exist is not None:
            return None
        user_created = Users.fromModel(user)
        session.add(user_created)
        session.commit()
        return user_created
    
    @staticmethod
    def getUsers(limit, page):
        print(limit, page)
        return session.query(Users).limit(limit).offset(limit*page)