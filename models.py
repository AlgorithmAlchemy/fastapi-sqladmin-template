# models.py
from sqlalchemy import Column, Integer, String, ForeignKey, Text
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()


class Category(Base):
    __tablename__ = "categories"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    products = relationship("Product", back_populates="category")

class Product(Base):
    __tablename__ = "products"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    category_id = Column(Integer, ForeignKey("categories.id"))  # <-- обязательно
    category = relationship("Category", back_populates="products")
    description = Column(Text)  # <- ЭТОГО НЕ ХВАТАЕТ В ТВОЁЙ МОДЕЛИ


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    username = Column(String, unique=True)
    email = Column(String, unique=True)
