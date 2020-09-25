from fastapi import APIRouter, Depends, HTTPException
from models import User, Organization, Leader
from logic.users import get_user
from pydantic import BaseModel
from tortoise.contrib.pydantic import pydantic_model_creator

router = APIRouter()
OrganizationModel = pydantic_model_creator(Organization)


class NewOrganization(BaseModel):
    name: str


async def get_organization(id: int):
    organization = await Organization.get_or_none(id=id)
    if organization is None:
        raise HTTPException(404, 'Not found')
    return organization


@router.post('/create')
async def create(organization: NewOrganization, user: User = Depends(get_user)):
    organization = await Organization.create(name=organization.name)
    await organization.leaders.add(await user.as_leader)


@router.get('/all')
async def get():
    return await OrganizationModel.from_queryset(Organization.all())
