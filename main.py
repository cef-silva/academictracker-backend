

from fastapi import FastAPI
from routers import user
from routers import course
from routers import material
from routers import university
from auth import authentication
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()



origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(user.router)
app.include_router(course.router)
app.include_router(authentication.router)
app.include_router(university.router)
app.include_router(material.router)




