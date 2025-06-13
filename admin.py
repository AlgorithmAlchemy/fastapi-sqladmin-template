# admin.py
from sqladmin import ModelView
from models import Product, Category, User



class ProductAdmin(ModelView, model=Product):
    name = "Товар"
    name_plural = "Товары"
    icon = "fa-solid fa-box"# admin.py
from sqladmin import ModelView
from models import Product, Category, User


class ProductAdmin(ModelView, model=Product):
    column_list = [Product.id, Product.name, Product.description]
    name = "Продукт"
    name_plural = "Продукты"
    icon = "fa-solid fa-box"


class CategoryAdmin(ModelView, model=Category):
    column_list = [Category.id, Category.name]
    name = "Категория"
    name_plural = "Категории"
    icon = "fa-solid fa-tags"


class UserAdmin(ModelView, model=User):
    column_list = [User.id, User.username, User.email]
    name = "Пользователь"
    name_plural = "Пользователи"
    icon = "fa-solid fa-user"