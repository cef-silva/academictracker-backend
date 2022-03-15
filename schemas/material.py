from pydantic import BaseModel, Field



from bson import ObjectId
from typing import List, Optional, Dict

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

class MateriaisBase(BaseModel):
    _idMateriais: ObjectId
    author: str
    title: str
    type_material: str
    year: str
    url: str
    descrição: str 
    detalhes: str 



class MateriaisDisplay(BaseModel):
    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")
    type_material: str = Field(alias="type")
    date: Optional[str]
    author: Optional[str]
    provider: Optional[str]
    title: Optional[str]
    duration: Optional[str]
    genre: Optional[str]
    description: Optional[str] 
    details: Optional[str] 
    thumb: Optional[str]
    rating: Optional[str]
    url: Optional[str]
    comments: Optional[List[Dict]]
    class Config():
        orm_mode=True
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}
    

class ArticleBase(BaseModel):
    _idArticle: ObjectId
    nomeArticle: str
    typeArticle: str
    descriptionArticle: str
    datePublish: str
    pdfArticle: str

class ArticleDisplay(BaseModel):
    id: PyObjectId = Field(default_factory=PyObjectId, alias="_idArticle")
    nomeArtigoTcc: str
    tipoArtigoTcc: str
    descricaoArtigoTcc: str
    dataPublicacao: str
    pdfArtigoTcc: str