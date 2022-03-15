from fastapi import APIRouter, Depends


from schemas.material import MateriaisBase, ArticleBase, MateriaisDisplay, ArticleDisplay
from database.db import conn


from auth.oauth2 import get_current_user

from typing import List

from schemas.user import UserAuth

from database.db import get_materiais_collection, get_article_collection

from repositories import material


router = APIRouter (
    prefix='/materiais',
    tags=['materiais']
)

@router.post('/', response_model= MateriaisDisplay)
def createMateriais(request: MateriaisBase, materiais= Depends(get_materiais_collection), current_user: UserAuth = Depends(get_current_user)):
    return material.registerMateriais(request, materiais)

@router.get('/', response_model = List[MateriaisDisplay])
def materiais(materiais = Depends(get_materiais_collection)):
    return material.get_all_materiais(materiais)

@router.get("/id", response_model=MateriaisDisplay)
def getmateriaisbyId(id:str, materiais=Depends(get_materiais_collection)):
    materialFound = material.get_by_id_material(id,materiais)
    return materialFound

