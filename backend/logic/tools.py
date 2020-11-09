import string
import random
from fastapi import HTTPException


def random_string(length=5):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for _ in range(length))


async def generate_link(model):
    counter = 5
    project_link = random_string(counter)
    while True:
        if await model.get_or_none(project_link=project_link) is None:
            break
        counter += 1
        project_link = random_string(counter)
    return project_link


async def instance_getter(model, **params):
    instance = await model.get_or_none(**params)
    if instance is None:
        raise HTTPException(404, f'{model.__name__} not found')
    return instance