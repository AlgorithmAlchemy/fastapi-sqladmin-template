import fastapi_admin
from fastapi_admin.app import app as admin_app
from fastapi_admin.providers.login import UsernamePasswordProvider
from starlette.requests import Request
from fastapi_admin.resources import Model
from fastapi_admin.widgets import displays, inputs
from models import Product
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "sqlite+aiosqlite:///./test.db"

engine = create_async_engine(DATABASE_URL, echo=True)
async_session = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)

class ProductAdmin(Model):
    label = "Продукты"
    model = Product
    page_pre_title = "Товары"
    page_title = "Управление товарами"
    icon = "fas fa-box"
    fields = [
        "id",
        inputs.Text(name="name", label="Название"),
        inputs.TextArea(name="description", label="Описание"),
    ]

async def on_mount():
    await fastapi_admin.app.init(
        admin_secret="supersecret",
        providers=[
            UsernamePasswordProvider(
                admin_model=None,
                login_logo_url="https://fastapi-admin.github.io/img/logo.png",
                logo_url="https://fastapi-admin.github.io/img/logo.png",
            )
        ],
        engine=engine,
        admin_path="/admin",
        resources=[ProductAdmin],
    )

admin_app.on_event("startup")(on_mount)
