from fastapi import APIRouter

app_user = APIRouter()

@app_user.get("/user")
async def get_name(user_id:int):
    print(user_id)
    user_name = user_id + "name"
    return {"user_name": user_name}
