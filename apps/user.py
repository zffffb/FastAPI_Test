from fastapi import APIRouter

user = APIRouter()

@user.get("/user")
async def get_name(user_id:int):
    print(user_id)
    user_name = user_id + "name"
    return {"user_name": user_name}
