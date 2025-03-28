from fastapi import FastAPI
import uvicorn
from fastapi.templating import Jinja2Templates

from api.user import app
from api.index import app

app = FastAPI()

templates = Jinja2Templates(directory="templates")

app.include_router(app,tags = ["user"])
app.include_router(app,tags = ["index"])

if __name__ == '__main__':
    uvicorn.run("main:app", port=8080, reload=True, log_level="debug") 