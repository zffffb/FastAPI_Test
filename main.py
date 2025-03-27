from fastapi import FastAPI
import uvicorn

from apps.user import user

app = FastAPI()

app.include_router(user,tags = ["user"])

if __name__ == '__main__':
    uvicorn.run("main:app", port=8080, reload=True, log_level="debug") 