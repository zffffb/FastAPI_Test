from fastapi import APIRouter
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


@user.post("/user/regin")
async def regin(user : User):
    return user