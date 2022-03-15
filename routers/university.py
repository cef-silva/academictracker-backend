from fastapi import APIRouter, Depends


from schemas.university import UniversityBase, GraduationBase, UniversityDisplay, GraduationDisplay, ProjectsBase, ProjectsDisplay
from database.db import conn


from auth.oauth2 import get_current_user

from typing import List

from schemas.user import UserAuth

from database.db import get_graduation_collection, get_university_collection, get_user_collection, get_projects_collection

from repositories import course


router = APIRouter (
    prefix='/university',
    tags=['university']
)

@router.post('/', response_model= UniversityDisplay)
def createUniversity(request: UniversityBase, university= Depends(get_university_collection), current_user: UserAuth = Depends(get_current_user)):
    return course.registerUniversity(request, university)

@router.get('/', response_model = List[UniversityDisplay])
def universities(university = Depends(get_university_collection)):
    return course.get_all_university(university)

@router.post('/graduation', response_model= GraduationDisplay)
def createGraduation(request: GraduationBase, graduation= Depends(get_graduation_collection), current_user: UserAuth = Depends(get_current_user)):
    return course.registerGraduation(request, graduation)

@router.get('/graduation', response_model= List[GraduationDisplay])
def graduations(graduation = Depends(get_graduation_collection)):
    return course.get_all_graduation(graduation)

@router.post('/projects', response_model=ProjectsDisplay)
def createProjects(request: ProjectsBase, project = Depends(get_projects_collection), current_user: UserAuth = Depends(get_current_user)):
    return course.registerProjects(request, project)

@router.get('/projects', response_model=List[ProjectsDisplay])
def project(project = Depends(get_projects_collection)):
    return course.get_all_projects(project)