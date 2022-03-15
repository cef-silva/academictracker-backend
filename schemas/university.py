from pydantic import BaseModel, Field



from bson import ObjectId
from typing import List, Optional

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

class UniversityBase(BaseModel):
    _id: ObjectId
    logoUniversidade: str
    universidade: str

class UniversityDisplay(BaseModel):
    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")
    logoUniversidade: str
    universidade: str
    class Config():
        orm_mode=True
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}

class GraduationBase(BaseModel):
    _idGraduation: ObjectId
    curso: str
    nomeUnivesidade: str
    descricao: str

class GraduationDisplay(BaseModel):
    id: PyObjectId = Field(default_factory=PyObjectId, alias="_idGraduation")
    curso: str
    nomeUnivesidade: str
    descricao: str
    class Config():
        orm_mode=True
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}

class ProjectsBase(BaseModel):
    _idProjects: ObjectId
    nomeProjects: str
    descricaoProject: str
    anoProject: str

class ProjectsDisplay(BaseModel):
    id: PyObjectId = Field(default_factory=PyObjectId, alias="_idProjects")
    nomeProjects: str
    descricaoProject: str
    anoProject: str
    class Config():
        orm_mode=True
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}
