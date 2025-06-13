# main.py
from fastapi import FastAPI
from admin import admin_app, provider, ProductAdmin
from config import DATABASE_URL, ADMIN_SECRET
from tortoise import Tortoise
from contextlib import asynccontextmanager

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Инициализация Tortoise ORM
    await Tortoise.init(
        db_url=DATABASE_URL,
        modules={"models": ["models"]}
    )
    await Tortoise.generate_schemas()

    # Инициализация FastAPI Admin
    await admin_app.init(
        admin_secret=ADMIN_SECRET,
        providers=[provider],
        resources=[ProductAdmin],
        admin_path="/admin",
        templates_dir="templates",
        login_footer="",
    )

    yield

    # Завершение Tortoise ORM
    await Tortoise.close_connections()

# Создание приложения с lifespan
app = FastAPI(lifespan=lifespan)

# Монтирование админки
app.mount("/admin", admin_app)
