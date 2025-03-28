from fastapi import APIRouter , Form
from typing import Union
from datetime import date
from pydantic import BaseModel , Field

app_user = APIRouter()

class User(BaseModel):
    name : str
    age : int = Field(default = 0 , gt = 0 , lt = 100)
    school : Union[str , None] =None
    major : Union[str , None] = None
    birth : Union[date , None] = None
    password : str 


@app_user.post("/regin")
async def regin(user : User):
    return user

@app_user.post("/login")
async def login(name : str = Form(),password : str = Form(min_length = 8,max_length = 16)):
    return True

@app_user.get("/home")
async def show_home():
    return 