from fastapi import FastAPI
import uvicorn

from apps.user import user

app = FastAPI()

app.include_router(app_user,tags = ["user"])

if __name__ == "__main__":
    uvicorn.run("main :app",reload = 8000) 