# main.py

from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from admin import admin_app
import models
from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.orm import sessionmaker

app = FastAPI()

# Static и Templates
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

# Admin
app.mount("/admin", admin_app)

# Роут на главную
@app.get("/", response_class=HTMLResponse)
async def read_index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

# Создание таблиц при старте
@app.on_event("startup")
async def startup_event():
    engine = create_async_engine("sqlite+aiosqlite:///./test.db", echo=True)
    async with engine.begin() as conn:
        await conn.run_sync(models.Base.metadata.create_all)
