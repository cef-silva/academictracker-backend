from fastapi import APIRouter, status, Depends

from fastapi.exceptions import HTTPException

from schemas.user import UserAuth
from database.db import conn

from database.hashing import Hash
from fastapi.security.oauth2 import  OAuth2PasswordRequestForm

from repositories import user as User


from auth.oauth2 import create_access_token


from database.db import get_user_collection

router = APIRouter (
    tags=['authentication']
)

@router.post('/login')
def login (request:OAuth2PasswordRequestForm = Depends ()):
    user = User.get_by_username (request.username, get_user_collection())
    if not user:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
        detail="Invalid Credentials")
    if not Hash.verify(request.password, user["password"]):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
        detail="Incorrect password")

    access_token = create_access_token(data={'username':user["username"], 'id':str(user["_id"])})
    return {
        'access_token' : access_token,
        'token_type' : 'bearer',
        'user_id' : str(user['_id']),
        'username' : user["username"]
    }