import os
import uvicorn
from fastapi import FastAPI
from tortoise.contrib.fastapi import register_tortoise
from starlette.middleware.cors import CORSMiddleware

import users
from settings import TORTOISE_ORM


for _dir in ['migrations', 'db']:
    if not os.path.isdir(_dir):
        os.mkdir(_dir)


app = FastAPI(
    version='0.0.1',
    title='Tasker',
    description='An example of full-stack service with auth',
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

if __name__ == '__main__':
    uvicorn.run('app:app', reload=True, use_colors=True)
