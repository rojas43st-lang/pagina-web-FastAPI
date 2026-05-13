from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()

# Archivos estáticos
app.mount("/static", StaticFiles(directory="static"), name="static")

# Templates
templates = Jinja2Templates(directory="templates")


@app.get("/")
async def home(request: Request):
    return templates.TemplateResponse(
        "index.html",
        {"request": request}
    )


@app.get("/modelos")
async def modelos(request: Request):
    return templates.TemplateResponse(
        "modelos.html",
        {"request": request}
    )


@app.get("/tecnologia")
async def tecnologia(request: Request):
    return templates.TemplateResponse(
        "tecnologia.html",
        {"request": request}
    )


@app.get("/historia")
async def historia(request: Request):
    return templates.TemplateResponse(
        "historia.html",
        {"request": request}
    )
    