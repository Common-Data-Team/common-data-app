from tortoise import Model, Tortoise
from tortoise import fields


class User(Model):
    id = fields.IntField(pk=True)
    email = fields.CharField(max_length=128, unique=True)
    hashed_password = fields.CharField(max_length=512)

    def __repr__(self):
        return str(self.email)

    class PydanticMeta:
        exclude = ['id', 'hashed_password']


Tortoise.init_models(["models"], "models")
