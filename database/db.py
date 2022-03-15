from pymongo import MongoClient
import os


client = MongoClient(os.getenv('MONGODB_URI'))
database_name =  os.getenv('MONGODB_NAME')

conn = client[database_name]

def get_user_collection ():
    return conn.users

def get_course_collection ():
    return conn.courses

def get_university_collection ():
    return conn.university

def get_materiais_collection ():
    return conn.material 

def get_article_collection ():
    return conn.article

def get_projects_collection ():
    return conn.projects

def get_graduation_collection ():
    return conn.graduation