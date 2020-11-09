from fastapi import APIRouter
from tortoise.contrib.pydantic import pydantic_model_creator, PydanticModel
from models import User
from pydantic import BaseModel
from typing import Optional, Any

router = APIRouter()
PublicUser = pydantic_model_creator(User, name='PublicUser')
PrivateUser = pydantic_model_creator(User, name='PrivateUser')


class NewUser(BaseModel):
    username: str


class Token(BaseModel):
    access_token: str
    token_type: str


class PublicHash(BaseModel):
    hash: str


class Success(BaseModel):
    ok: bool
    payload: Optional[Any] = None


class EditGroup(BaseModel):
    title: Optional[str] = None
    public: Optional[bool] = None
