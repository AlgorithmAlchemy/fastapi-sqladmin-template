# admin.py
from sqladmin import ModelView
from models import Product, Category, User


class ProductAdmin(ModelView, model=Product):
    column_list = [Product.id, Product.name, Product.description]
    name = "Product"
    name_plural = "Products"
    icon = "fa fa-box"


class CategoryAdmin(ModelView, model=Category):
    column_list = [Category.id, Category.name]
    name = "Category"
    name_plural = "Categories"
    icon = "fa fa-tags"


class UserAdmin(ModelView, model=User):
    column_list = [User.id, User.username, User.email]
    name = "User"
    name_plural = "Users"
    icon = "fa fa-user"
