# models.py

from tortoise import fields
from tortoise.models import Model
from fastapi_admin.models import AbstractAdmin

class Product(Model):
    id = fields.IntField(pk=True)
    name = fields.CharField(max_length=255)
    description = fields.TextField(null=True)

    def __str__(self):
        return self.name

class AdminUser(AbstractAdmin):
    pass
