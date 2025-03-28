from fastapi import FastAPI
import uvicorn
from fastapi.templating import Jinja2Templates

from api.user import app_user
from api.index import app_index

app = FastAPI()


app.include_router(app_user,prefix = "/user",tags = ["user"])
app.include_router(app_index,prefix = "/index",tags = ["index"])

if __name__ == '__main__':
    uvicorn.run("main:app", port=8080, reload=True, log_level="debug") 