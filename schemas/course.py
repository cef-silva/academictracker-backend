from pydantic import BaseModel, Field



from bson import ObjectId
from typing import List, Optional, Dict
from schemas.user import UserBase
from schemas.university import ProjectsDisplay
from schemas.material import MateriaisDisplay, ArticleDisplay

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


class CourseBase(BaseModel):
    _id: ObjectId
    URL: str
    description: str
    publisher: str
    details: str
    typeCourse: str
    title: str
    image: str
    rating: float
    numAulas: str
    duracaoTotal: str
    author: str

class CourseDisplay(BaseModel):
    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")
    title: str
    author: Optional[str]
    genre: Optional[str]
    date: Optional[str]
    author: Optional[str]
    duration:Optional[str]
    classes: Optional[str]
    description: str
    details: str
    thumb: Optional[str]
    url: Optional[str]
    rating: Optional[str]
    comments: Optional[List[Dict]]
    class Config():
        orm_mode=True
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}


class Disciplinas(BaseModel): 
    _idDisciplinas: ObjectId
    nomeDisciplina: str
    anoDisciplina: str

class Activities(BaseModel):
    projetos: Optional[ProjectsDisplay]
    artigos: Optional[ArticleDisplay]
    livros: Optional[MateriaisDisplay]




