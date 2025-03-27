from fastapi import APIRouter
from typing import Union
from datetime import date

user = APIRouter()

@user.get("/user")
async def get_info(user_name:str,
                   user_birth:Union[date,None] = None,
                   user_school:Union[str,None] = None):
    print(user_name,user_birth,user_school)
    return {"user_name": user_name,"user_birth": user_birth,"user_school": user_school}
