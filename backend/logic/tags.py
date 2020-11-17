from fastapi import APIRouter
from tortoise.contrib.pydantic import pydantic_model_creator
from models import Tag

router = APIRouter()
PublicTags = pydantic_model_creator(Tag, include=('name', 'projects'))


@router.get('/all')
async def all_tags():
    return await PublicTags.from_queryset(Tag.all())
