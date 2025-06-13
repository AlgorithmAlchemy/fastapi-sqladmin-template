# admin.py
from fastapi_admin.app import app as admin_app
from fastapi_admin.providers.login import UsernamePasswordProvider
from fastapi_admin.resources import Model as AdminModel, Field
from fastapi_admin.widgets import inputs
from models import Product

from sqladmin import ModelView
from models import Product, Category, User



class ProductAdmin(ModelView, model=Product):
    name = "Товар"
    name_plural = "Товары"
    icon = "fa-solid fa-box"
    category = "🛒 Магазин"
    column_list = [Product.id, Product.name, Product.description]
    column_searchable_list = [Product.name, Product.description]
    column_filters = [Product.name]


class CategoryAdmin(ModelView, model=Category):
    name = "Категория"
    name_plural = "Категории"
    icon = "fa-solid fa-tags"
    category = "🛒 Магазин"
    column_list = [Category.id, Category.title]
    column_searchable_list = [Category.title]
    column_filters = [Category.title]


class UserAdmin(ModelView, model=User):
    name = "Пользователь"
    name_plural = "Пользователи"
    icon = "fa-solid fa-user"
    category = "⚙️ Администрирование"
    column_list = [User.id, User.username]
    column_searchable_list = [User.username]


