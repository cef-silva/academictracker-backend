from fastapi import APIRouter, Depends, HTTPException

from schemas.user import UserDisplay, UserBase


from database.db import get_user_collection, get_university_collection

from repositories import user

from typing import List



router = APIRouter (
    prefix='/user',
    tags=['user']
)


@router.post('/', response_model=UserDisplay )
def create(request: UserBase, users = Depends(get_user_collection), universities= Depends(get_university_collection)):
    userFound = user.get_by_username(request.username,users)

    if (userFound):
        raise HTTPException(status_code=400,
                            detail='Usuario Existente')
    else:
        return user.create(request, users)


@router.get("/", response_model=List[UserDisplay])
def users(users = Depends(get_user_collection)):
    return user.get_all(users)

@router.put("/id/edit-university")
def edit_university(id: str, faculdade: str, users = Depends(get_user_collection)):
    user.edit_university( id, faculdade, users)
    return {"mensagem": "Universidade Atualizada"}

@router.put("/id/edit-graduation")
def edit_graduation(id: str, graduation: str, users = Depends(get_user_collection)):
    user.edit_graduation( id, graduation, users)
    return {"mensagem": "Graduação atualizada"}

@router.put("/id/edit-about")
def edit_about( id: str, about:str, users = Depends(get_user_collection)):
    user.edit_about( id, about, users)
    return {"mensagem": "About foi atualizado"}

@router.put("/id/edit-profpic")
def edit_profpic( id: str, profilePicture:str, users = Depends(get_user_collection)):
    user.edit_profpic( id, profilePicture, users)
    return {"mensagem": "Foto de Perfil foi atualizada"}

@router.get("/id", response_model=UserDisplay)
def getbyid(id:str, users=Depends(get_user_collection)):
   userFound = user.get_by_id(id,users)
   return userFound


