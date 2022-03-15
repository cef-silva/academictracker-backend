# https://fastapi.tiangolo.com/tutorial/security/oauth2-jwt/


from jose import jwt, JWTError
from datetime import datetime, timedelta

from fastapi import HTTPException, Depends, status

from repositories import user as User

from fastapi.security import OAuth2PasswordBearer

from database.db import get_user_collection

#generate hash
SECRET_KEY = '6b25ca08a80b2f7c828805b19399551a14166560c87f6e1ea9221b059df52126'
ALGORITHM = 'HS256'
ACCESS_TOKEN_EXPIRE_MINUTES = 30

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")

def create_access_token(data: dict):
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

def get_current_user(token: str = Depends(oauth2_scheme)):
    
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("username")
        if username is None:
            raise credentials_exception
    except JWTError:
        raise credentials_exception
    user =  User.get_by_username(username, get_user_collection())
    if user is None:
        raise credentials_exception
    return user