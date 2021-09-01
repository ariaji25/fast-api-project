"""Auth Extention.

Auth extention created cause, when any auth function needed for
another view controll, this extention is easly to call.

"""

from fastapi.security import OAuth2PasswordBearer
from fastapi import Depends, HTTPException, status

from .models import AuthToken, Users
from .schemas import TokenData


# o2auth scheme, defined the o2auth url
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="api/v1/auth/login")

# credential response exception when token is unauthorized
credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"})

def get_current_user(token : str = Depends(oauth2_scheme)):
        try:
            payload = AuthToken.get_token_payload(token)
            username : str = payload.get("sub")
            if username is None:
                raise credentials_exception
            token_data = TokenData(username=username)
        except Exception as e:
            raise credentials_exception
        user = Users.exist(Users.email==token_data.username)
        return user

def get_superadmin(token : str = Depends(oauth2_scheme)):
        try:
            payload = AuthToken.get_token_payload(token)
            username : str = payload.get("sub")
            if username is None:
                raise credentials_exception
            token_data = TokenData(username=username)
        except Exception as e:
            raise credentials_exception
        user:Users= Users.exist(Users.email==token_data.username)
        if user.role == 'ludes.superadmin' :
            return user
        else:
            raise credentials_exception