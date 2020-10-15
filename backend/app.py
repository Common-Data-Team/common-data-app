import os
import uvicorn
from fastapi import FastAPI
from tortoise.contrib.fastapi import register_tortoise
from starlette.middleware.cors import CORSMiddleware
from logic import users, organizations, projects
from settings import TORTOISE_ORM


for _dir in ['db']:
    if not os.path.isdir(_dir):
        os.mkdir(_dir)


app = FastAPI(
    version='0.0.1',
    title='Data App',
    description='API for the Common Data app based on FastAPI',
)

register_tortoise(
    app,
    config=TORTOISE_ORM,
    generate_schemas=True,
    add_exception_handlers=True,
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
    organizations.router,
    prefix='/organizations',
    tags=['Organizations']
)

app.include_router(
    projects.router,
    prefix='/projects',
    tags=['Projects']
)


if __name__ == '__main__':
    uvicorn.run('app:app', reload=True, use_colors=True)
