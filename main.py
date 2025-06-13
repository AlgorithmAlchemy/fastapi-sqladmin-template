# main.py
from fastapi import FastAPI
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker
from sqladmin import Admin, ModelView

from models import Base, Product

DATABASE_URL = "sqlite+aiosqlite:///./test.db"

engine = create_async_engine(DATABASE_URL, echo=True)
async_session_maker = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)

app = FastAPI()


# Создаём таблицы при запуске
@app.on_event("startup")
async def on_startup():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)


# Админка
class ProductAdmin(ModelView, model=Product):
    column_list = [Product.id, Product.name, Product.description]
    name = "Product"
    name_plural = "Products"
    icon = "fa fa-box"

admin = Admin(app, engine)
admin.add_view(ProductAdmin)
