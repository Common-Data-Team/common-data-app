from fastapi import APIRouter, HTTPException
from tortoise.contrib.pydantic import pydantic_model_creator
from models import Tag
from typing import List

router = APIRouter()
excluded = (
    'projects.questionnaire',
    'projects.markdown',
    'projects.creation_date',
    'projects.members',
    'projects.leaders',
)
included = ()
PublicTags = pydantic_model_creator(Tag, exclude=excluded)
OnlyName = pydantic_model_creator(Tag, include=('name', ))


@router.get('/all', response_model=List[str])
async def all_tags():
    return [tag.name for tag in await Tag.all()]


@router.get('/{name}', response_model=PublicTags)
async def all_tags(name: str):
    tag = await Tag.get_or_none(name=name)
    if tag is None:
        raise HTTPException(404, 'Tag not found')
    return await PublicTags.from_tortoise_orm(tag)
