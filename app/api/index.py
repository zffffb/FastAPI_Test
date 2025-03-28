from fastapi import APIRouter , Request
from fastapi.templating import Jinja2Templates

app = APIRouter()

templates = Jinja2Templates(directory="templates")

@app.get("/index")
async def index(request : Request):
    return templates.TemplateResponse(
        "index.html",
        {
            "request" : request
        }
    )