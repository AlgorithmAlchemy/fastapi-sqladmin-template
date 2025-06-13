from fastapi import FastAPI
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker
from sqladmin import Admin
from models import Base, Product, Category, User
from admin import ProductAdmin, CategoryAdmin, UserAdmin

DATABASE_URL = "sqlite+aiosqlite:///./test.db"
engine = create_async_engine(DATABASE_URL, echo=True)
async_session_maker = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)

app = FastAPI()

@app.on_event("startup")
async def startup():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)

admin = Admin(app, engine)
admin.add_view(ProductAdmin)
admin.add_view(CategoryAdmin)
admin.add_view(UserAdmin)
