# main.py
# main.py
from fastapi import FastAPI
from sqladmin import Admin
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker

from models import Base
from admin import ProductAdmin, CategoryAdmin, UserAdmin

DATABASE_URL = "sqlite+aiosqlite:///./test.db"

# Async SQLAlchemy setup
engine = create_async_engine(DATABASE_URL, echo=True, future=True)
async_session_maker = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)

# FastAPI app
app = FastAPI(
    title="Brand eCommerce",
    description="Интерфейс администрирования и API для интернет-магазина",
    version="1.0.0"
)

# Admin panel
admin = Admin(app=app, engine=engine)
admin.add_view(ProductAdmin)
admin.add_view(CategoryAdmin)
admin.add_view(UserAdmin)

# Создание таблиц при запуске
@app.on_event("startup")
async def on_startup():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
