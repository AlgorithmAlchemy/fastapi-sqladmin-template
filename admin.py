# admin.py
from fastapi_admin.app import app as admin_app
from fastapi_admin.providers.login import UsernamePasswordProvider
from fastapi_admin.resources import Model as AdminModel, Field
from fastapi_admin.widgets import inputs
from models import Product, AdminUser

class ProductAdmin(AdminModel):
    label = "Товары"
    model = Product
    page_pre_title = "Товары"
    page_title = "Управление товарами"
    icon = "fas fa-box"
    fields = [
        Field("id", "ID", input_=inputs.DisplayOnly()),
        Field("name", "Название", input_=inputs.Text()),
        Field("description", "Описание", input_=inputs.TextArea()),
    ]

provider = UsernamePasswordProvider(
    admin_model=AdminUser,
    login_logo_url="https://fastapi-admin.github.io/img/logo.png",
)