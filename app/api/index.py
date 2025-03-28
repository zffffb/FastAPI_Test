from fastapi import APIRouter , Request
from fastapi.templating import Jinja2Templates

app_index = APIRouter()

templates = Jinja2Templates(directory="templates")

@app_index.get("/index")
async def index(request : Request):
    return templates.TemplateResponse(
        "index.html",
        {
            "request" : request
        }
    )