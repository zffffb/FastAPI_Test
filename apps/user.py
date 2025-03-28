from fastapi import APIRouter , Form
from typing import Union
from datetime import date
from pydantic import BaseModel , Field

user = APIRouter()

class User(BaseModel):
    name : str
    age : int = Field(default = 0 , gt = 0 , lt = 100)
    school : Union[str , None] =None
    major : Union[str , None] = None
    birth : Union[date , None] = None
    password : str 


@user.post("/user/regin")
async def regin(user : User):
    return user

@user.post("/user/login")
async def login(name : str = Form(),password : str = Form(min_length = 8,max_length = 16)):
    return True

@user.get("/user/home")
async def show_home():
    return 