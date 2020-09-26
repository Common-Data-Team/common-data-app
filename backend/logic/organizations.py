from typing import Optional
from fastapi import APIRouter, Depends, HTTPException, Body
from models import User, Organization, Leader
from logic.users import get_user
from logic.tools import generate_link, instance_getter
from pydantic import BaseModel, Field
from tortoise.contrib.pydantic import pydantic_model_creator

router = APIRouter()
PrivateOrganization = pydantic_model_creator(Organization)
PublicOrganization = pydantic_model_creator(Organization, exclude=())


class New(BaseModel):
    name: str
    description: str


class Edit(BaseModel):
    name: str
    description: str


async def org_by_id(id: int) -> Organization:
    return await instance_getter(Organization, id=id)


async def org_by_link(link: str) -> Organization:
    return await instance_getter(Organization, link=link)


@router.post('/create', response_model=PrivateOrganization)
async def create(created: New, user: User = Depends(get_user)):
    link = await generate_link(Organization)
    organization = await Organization.create(**created.dict(), link=link)
    await organization.leaders.add(await user.as_leader)
    return await PrivateOrganization.from_tortoise_orm(organization)


@router.put('/{link}/edit', response_model=PrivateOrganization)
async def edit(organization: Organization = Depends(org_by_link),
               user: User = Depends(get_user),
               edited: Edit = Body(...)):
    if await organization.leaders.filter(user=user):
        organization = await organization.update_from_dict(edited.dict())
        await organization.save()
        return await PrivateOrganization.from_tortoise_orm(organization)
    raise HTTPException(403, 'Access denied')


@router.get('/all')
async def get():
    return await PrivateOrganization.from_queryset(Organization.all())


@router.post('/{link}/enter')
async def enter(link: str, user: User = Depends(get_user)):
    organization: Organization = await org_by_link(link)
    await organization.members.add(await user.as_member)
    return await PublicOrganization.from_tortoise_orm(organization)


@router.get('/{link}', response_model=PublicOrganization)
async def show(link: str):
    organization: Organization = await org_by_link(link)
    return await PublicOrganization.from_tortoise_orm(organization)


# @router.post('/{link}')
# async def update(organization: Organization = Depends(org_by_link),
#                  edited: Edit = Body(...),
#                  user: User = Depends(get_user)):
    # organization
