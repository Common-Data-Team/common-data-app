from tortoise import Model, Tortoise
from tortoise import fields


class User(Model):
    id = fields.IntField(pk=True)
    email = fields.CharField(max_length=128, unique=True)
    hashed_password = fields.CharField(max_length=512)

    fio = fields.CharField(null=True, max_length=128)
    level = fields.IntField(default=0)
    avatar = fields.CharField(null=True, max_length=256)
    about = fields.TextField(default='Инфомация обо мне')
    is_admin = fields.BooleanField(default=False)
    # social_networks = fields.TextField()

    tags = fields.ManyToManyField('models.Tag')

    as_member: fields.ReverseRelation['Member']
    as_leader: fields.ReverseRelation['Leader']
    favourite_projects: fields.ManyToManyRelation['Project']

    def __repr__(self):
        return str(self.email)

    class PydanticMeta:
        exclude = ['id', 'hashed_password', 'is_admin']


class Member(Model):
    id = fields.IntField(pk=True)
    user = fields.OneToOneField('models.User', 'as_member')
    projects: fields.ManyToManyRelation['Project']


class Leader(Model):
    id = fields.IntField(pk=True)
    user = fields.OneToOneField('models.User', 'as_leader')
    projects: fields.ManyToManyRelation['Project']


class Project(Model):
    id = fields.IntField(pk=True)
    title = fields.CharField(max_length=128)
    project_link = fields.CharField(max_length=64)
    participants_target = fields.IntField()

    questionnaire_link = fields.CharField(null=True, max_length=256)
    is_active = fields.BooleanField(default=True)
    markdown = fields.TextField(default="# Вы можете редактировать содержимое страницы")
    creation_date = fields.DatetimeField(auto_now_add=True)
    description = fields.TextField(null=True)
    participants_count = fields.IntField(default=0)
    project_img = fields.CharField(256, null=True)

    members = fields.ManyToManyField('models.Member', related_name='projects')
    leaders = fields.ManyToManyField('models.Leader', related_name='projects')
    tags: fields.ManyToManyRelation['Tag']


class Tag(Model):
    id = fields.IntField(pk=True)
    name = fields.CharField(max_length=64)
    projects = fields.ManyToManyField('models.Project', related_name='tags')
    users: fields.ManyToManyRelation['User']


Tortoise.init_models(["models"], "models")
