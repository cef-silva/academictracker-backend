

from schemas.user import UserBase
from database.hashing import Hash

from database.db import conn

from fastapi import Depends

from bson import ObjectId

from database.db import get_user_collection, get_university_collection

def create (request: UserBase, users):
    new_user = request.dict(by_alias=True)
    new_user["password"] = Hash.bcrypt (new_user["password"])
    conn.users.insert_one(new_user)
    return new_user


def get_all(users):  
    return list(users.find())

def edit_about(id:str,about: str, ids= Depends(get_user_collection)):
    newAbout = ids.update_one({"_id": ObjectId(id)}, {"$set":{"about": about}})
    return newAbout

def edit_university(id:str, faculdade: str, ids = Depends(get_user_collection)):
    newUniversity = ids.update_one({"_id": ObjectId(id)}, {"$set":{"faculdade":faculdade}})
    return newUniversity

def edit_graduation(id:str, curso: str, ids = Depends(get_user_collection)):
    newGraduation = ids.update_one({"_id": ObjectId(id)}, {"$set":{"curso":curso}})
    return newGraduation

def edit_profpic(id:str,profilePicture: str, ids= Depends(get_user_collection)):
    newPicture = ids.update_one({"_id": ObjectId(id)}, {"$set":{"profilePicture": profilePicture}})
    return newPicture

def get_by_username(username: str, users = Depends(get_user_collection)):
    user = users.find_one({'username':username})
    return user

def get_by_id(id: str, ids = Depends(get_user_collection)):
    id = ids.find_one({'_id':ObjectId(id)})
    return id


