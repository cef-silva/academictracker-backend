
from schemas.course import CourseBase, CourseDisplay
from schemas.university import UniversityBase, ProjectsBase, GraduationBase
from schemas.material import ArticleBase
from database.db import get_course_collection, get_user_collection, get_university_collection, get_article_collection, get_graduation_collection, get_projects_collection

from fastapi import Depends
from bson import ObjectId



def createCourse (request: CourseBase, courses):
    new_course = request.dict(by_alias=True)
    courses.insert_one(new_course)
    return request

def registerUniversity (request: UniversityBase, university):
    new_university = request.dict(by_alias=True)
    university.insert_one(new_university)
    return request

def registerArticle (request: ArticleBase, article):
    new_article = request.dict(by_alias=True)
    article.insert_one(new_article)
    return request

def registerGraduation (request: GraduationBase, graduation):
    new_graduation = request.dict(by_alias=True)
    graduation.insert_one(new_graduation)
    return request

def registerProjects (request: ProjectsBase, project):
    new_project = request.dict(by_alias=True)
    project.insert_one(new_project)
    return request

def get_all_university(university):
    return list(university.find())

def get_all_graduation(graduation):
    return list(graduation.find())
    
def get_all_article(article):
    return list(article.find())

def get_all_projects(project):
    return list(project.find())

def get_all(courses):  
    return list(courses.find())

def get_by_id_curso(id: str, ids = Depends(get_course_collection)):
    id = ids.find_one({'_id':ObjectId(id)})
    return id


