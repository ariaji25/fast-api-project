"""Class Models for Users.

All transaction to table Users, must defined here

"""


from datetime import datetime

from passlib.context import CryptContext 
from datetime import datetime
from sqlalchemy import *
from sqlalchemy.orm import relationship

from database import Base, session
from .schemas import UserModel


passwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


class EnumRole:
    SUPER_ADMIN = "ludes.superadmin"
    ADMIN = "ludes.admin"
    MERCENT_ADMIN = "ludes.mercent.admin"
    MERCENT_CASHIER = "ludes.mercent.cashier"

class EnumBussinesType:
    CAFE = "cafe"
    STORE = "store"

class Users(Base):

    __tablename__ = "users"
    
    id = Column(Integer,primary_key=True, index=True)
    name = Column(String, nullable=False, default="My Name")
    email = Column(String, nullable=False, unique=True, index=True, default="test@mail.com")
    password = Column(String, nullable=False, default="password")
    hashed_password = Column(String, nullable=False, default=passwd_context.hash("password"))
    bussines_name = Column(String, nullable=False, default="My Bussiness")
    bussines_type = Column(String, default=EnumBussinesType.CAFE)
    role = Column(String, nullable=False, default=EnumRole.ADMIN)
    is_active = Column(Boolean, default=False)
    is_super = Column(Boolean, default=False)
    is_verified = Column(Boolean, default=False)
    created_at = Column(DateTime, default=datetime.now())
    updated_at = Column(DateTime, default=datetime.now())
    token = relationship('AuthToken', back_populates='user')

    @staticmethod
    def exist(*args, **kwargs):
        return session.query(Users).filter(*args, **kwargs).first()

    @staticmethod
    def get_hash_password(password : str) -> str:
        return passwd_context.hash(password)
    
    def verify_password(self, password):
        return passwd_context.verify(password, self.hashed_password)

    @staticmethod
    def fromModel(user : UserModel):
        return Users(
            name=user.name,
            email=user.email,
            password=user.password,
            hashed_password=Users.get_hash_password(user.password),
            bussines_name=user.bussines_name,
            bussines_type=user.bussines_type,
            created_at = datetime.now(),
            updated_at = datetime.now()
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
        return session.query(Users).limit(limit).offset(limit*page).all()