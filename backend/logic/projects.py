from fastapi import APIRouter, Depends, Body, HTTPException, Query
from models import Project, User, Organization
from pydantic import BaseModel, Field
from tortoise.contrib.pydantic import pydantic_model_creator, pydantic_queryset_creator
from logic.users import get_user
from logic.tools import generate_link, instance_getter
from logic.organizations import org_by_link

PrivateProject = pydantic_model_creator(Project)
PublicProject = pydantic_model_creator(Project)
router = APIRouter()


class New(BaseModel):
    name: str = Field(max_length=128)
    description: str


class Edit(BaseModel):
    name: str = Field(max_length=128)
    description: str


async def project_by_link(link: str):
    return await instance_getter(Project, link=link)


@router.post('/create')
async def create(
        new_project: New = Body(...),
        organization: Organization = Depends(org_by_link),
        user: User = Depends(get_user)):

    if await organization.leaders.filter(user=user):
        link = await generate_link(Project)
        project = await Project.create(**new_project.dict(), link=link, organization=organization)
        return await PrivateProject.from_tortoise_orm(project)
    raise HTTPException(403, 'Access denied')


@router.put('/{link}/edit', response_model=PrivateProject)
async def edit(project: Project = Depends(project_by_link),
               user: User = Depends(get_user),
               edited: Edit = Body(...)):
    if await (await project.organization).leaders.filter(user=user):
        project = await project.update_from_dict(edited.dict())
        await project.save()
        return await PrivateProject.from_tortoise_orm(project)
    raise HTTPException(403, 'Access denied')


@router.get('/all')
async def get():
    return await PrivateProject.from_queryset(Project.all())


@router.post('/{link}/enter')
async def enter(link: str, user: User = Depends(get_user)):
    project: Project = await project_by_link(link)
    await project.members.add(await user.as_member)
    return await PublicProject.from_tortoise_orm(project)


@router.get('/{link}', response_model=PublicProject)
async def show(link: str):
    project: Project = await project_by_link(link)
    return await PublicProject.from_tortoise_orm(project)


@router.get('/all')
async def get_all():
    return await PrivateProject.from_queryset(Project.all())
