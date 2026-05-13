from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")


@app.get("/")
async def home(request: Request):
    return templates.TemplateResponse(
        request,
        "index.html"
    )


@app.get("/modelos")
async def modelos(request: Request):
    return templates.TemplateResponse(
        request,
        "modelos.html"
    )


@app.get("/tecnologia")
async def tecnologia(request: Request):
    return templates.TemplateResponse(
        request,
        "tecnologia.html"
    )


@app.get("/historia")
async def historia(request: Request):
    return templates.TemplateResponse(
        request,
        "historia.html"
    )