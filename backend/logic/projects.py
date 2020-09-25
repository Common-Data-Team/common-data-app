from fastapi import APIRouter, Depends, Body, HTTPException
from models import Project, User, Organization
from pydantic import BaseModel, Field
from tortoise.contrib.pydantic import pydantic_model_creator, pydantic_queryset_creator
from logic.organizations import get_organization
from logic.users import get_user


class NewProject(BaseModel):
    title: str = Field(max_length=128)
    description: str


PrivateProject = pydantic_model_creator(Project)
router = APIRouter()


@router.post('/create')
async def create(
        new_project: NewProject,
        organization: Organization = Depends(get_organization),
        user: User = Depends(get_user)):
    if await organization.leaders.filter(user=user):
        project = await Project.create(**new_project.dict(), organization=organization)
        return await PrivateProject.from_tortoise_orm(project)
    raise HTTPException(403, 'Access denied')

# @router.post('/enter')
# async def enter():

@router.get('/all')
async def get_all():
    return await PrivateProject.from_queryset(Project.all())
