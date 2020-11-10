import os
import contextvars
import logging
import uvicorn
import shutil
from pathlib import Path
from fastapi import FastAPI
from tortoise.contrib.fastapi import register_tortoise
from tortoise import Tortoise
from starlette.middleware.cors import CORSMiddleware
from logic import users, projects, tags
from settings import PROD_TORTOISE_ORM, TEST_TORTOISE_ORM
from fill_db import fill_tags


app = FastAPI(
    version='0.0.1',
    title='Data App',
    description='API for the Common Data app based on FastAPI',
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(
    users.router,
    prefix='/users',
    tags=['Users']
)

app.include_router(
    projects.router,
    prefix='/projects',
    tags=['Projects']
)

app.include_router(
    tags.router,
    prefix='/tags',
    tags=['Tags']
)


# config_var = TEST_TORTOISE_ORM
config_var = PROD_TORTOISE_ORM

shutil.rmtree('db/test')  # Удаляем папку с тестовой базой данных при запуске и импорте
for path in ['db/test', 'db/prod']:
    Path(path).mkdir(parents=True, exist_ok=True)


@app.on_event('startup')
async def startup():
    await Tortoise.init(config=config_var)
    await Tortoise.generate_schemas(safe=True)
    await fill_tags()


if __name__ == '__main__':
    uvicorn.run('app:app', reload=True, use_colors=True)
