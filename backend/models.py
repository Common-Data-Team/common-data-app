from tortoise import Model, Tortoise
from tortoise import fields


class User(Model):
    id = fields.IntField(pk=True)
    email = fields.CharField(max_length=128, unique=True)
    hashed_password = fields.CharField(max_length=512)

    # Project based fields
    fio = fields.CharField(null=True, max_length=128)
    level = fields.IntField(default=0)
    is_admin = fields.BooleanField(default=False)
    # social_networks = fields.TextField()

    as_member: fields.ReverseRelation['Member']
    as_leader: fields.ReverseRelation['Leader']
    # Relations

    favourite_projects: fields.ManyToManyRelation['Project']

    def __repr__(self):
        return str(self.email)

    class PydanticMeta:
        exclude = ['id', 'hashed_password']


class Member(Model):
    id = fields.IntField(pk=True)
    user = fields.OneToOneField('models.User', 'as_member')
    organizations_member: fields.ManyToManyRelation['Organization']
    projects_member: fields.ManyToManyRelation['Project']


class Leader(Model):
    id = fields.IntField(pk=True)
    user = fields.OneToOneField('models.User', 'as_leader')
    organizations: fields.ManyToManyRelation['Organization']
    projects: fields.ManyToManyRelation['Project']


class Organization(Model):
    id = fields.IntField(pk=True)
    verified = fields.BooleanField(default=False)
    name = fields.CharField(max_length=128)
    members = fields.ManyToManyField('models.User', related_name='organizations_member')
    leaders = fields.ManyToManyField('models.Leader', related_name='organizations_leader')

    projects: fields.ReverseRelation['Project']


class FieldOfInterest(Model):
    id = fields.IntField(pk=True)


class Project(Model):
    id = fields.IntField(pk=True)
    title = fields.CharField(max_length=128)
    description = fields.TextField()

    members = fields.ManyToManyField('models.User', related_name='projects_member')
    leaders = fields.ManyToManyField('models.Leader', related_name='projects_leader')
    organization = fields.ForeignKeyField('models.Organization', related_name='projects')
    tags: fields.ManyToManyRelation['Tag']


class Tag(Model):
    id = fields.IntField(pk=True)
    name = fields.CharField(max_length=64)
    projects = fields.ManyToManyField('models.Project', related_name='tags')


Tortoise.init_models(["models"], "models")
