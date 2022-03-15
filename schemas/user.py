from pydantic import BaseModel, Field


from typing import List, Optional
from bson import ObjectId
from schemas.university import UniversityBase

class PyObjectId(ObjectId):
    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, v):
        if not ObjectId.is_valid(v):
            raise ValueError("Invalid objectid")
        return ObjectId(v)

    @classmethod
    def __modify_schema__(cls, field_schema):
        field_schema.update(type="string")

class UserBase(BaseModel):
    _id: ObjectId
    name: str
    username: str
    profilePicture: Optional[str]
    about: Optional[str]
    faculdade: Optional[str]
    curso: Optional[str]
    password: str

class UserBasicDisplay(BaseModel):
    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")
    name: str
    username: str
    class Config():
        orm_mode=True

class UserDisplay(BaseModel):
    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")
    name: str
    username: str
    profilePicture: Optional[str]
    about: Optional[str]
    faculdade: Optional[str]
    curso: Optional[str]
    undergraduate: Optional[UniversityBase]
    class Config():
        orm_mode=True
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}

class UserAuth(BaseModel):
    username:str
    password:str

