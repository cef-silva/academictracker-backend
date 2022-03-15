from fastapi import APIRouter, Depends

from schemas.course import CourseDisplay, CourseBase
from schemas.user import UniversityBase
from database.db import conn


from auth.oauth2 import get_current_user

from typing import List

from schemas.user import UserAuth

from database.db import get_course_collection, get_university_collection, get_user_collection

from repositories import course


router = APIRouter (
    prefix='/course',
    tags=['course']
)


@router.post('/', response_model=CourseDisplay)
def createCourse(request: CourseBase, courses = Depends(get_course_collection), current_user: UserAuth = Depends(get_current_user) ):
    return course.createCourse(request, courses)

@router.get("/", response_model=List[CourseDisplay])
def courseShow(courses = Depends(get_course_collection)):
    return course.get_all(courses)

@router.get("/id", response_model=CourseDisplay)
def getcoursebyId(id:str, courses=Depends(get_course_collection)):
    courseFound = course.get_by_id_curso(id,courses)
    return courseFound


