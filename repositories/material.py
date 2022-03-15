from database.db import get_materiais_collection
from schemas.material import MateriaisBase


from fastapi import Depends
from bson import ObjectId

def registerMateriais(request: MateriaisBase, materiais):
    new_materiais = request.dict(by_alias=True)
    materiais.insert_one(new_materiais)
    return request

def get_by_id_material(id: str, ids = Depends(get_materiais_collection)):
    id = ids.find_one({'_id':ObjectId(id)})
    return id

def get_all_materiais(material):
    return list(material.find())
