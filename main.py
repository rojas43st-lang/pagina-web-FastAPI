from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent

app = FastAPI()

app.mount(
    "/static",
    StaticFiles(directory=str(BASE_DIR / "static")),
    name="static"
)

templates = Jinja2Templates(
    directory=str(BASE_DIR / "templates")
)

@app.get("/", response_class=HTMLResponse)
async def inicio(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="index.html",
        
    )

@app.get("/modelos", response_class=HTMLResponse)
async def modelos(request: Request):
    return templates.TemplateResponse(
        "modelos.html",
        {"request": request}
    )

@app.get("/tecnologia", response_class=HTMLResponse)
async def tecnologia(request: Request):
    return templates.TemplateResponse(
        "tecnologia.html",
        {"request": request}
    )

@app.get("/historia", response_class=HTMLResponse)
async def historia(request: Request):
    return templates.TemplateResponse(
        "historia.html",
        {"request": request}
    )
