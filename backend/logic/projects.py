from fastapi import APIRouter, Depends, Body, HTTPException, Query
from models import Project, User, Tag
from pydantic import BaseModel, Field
from tortoise.contrib.pydantic import pydantic_model_creator, pydantic_queryset_creator
from logic.users import get_user
from logic.tools import generate_link, instance_getter, m2m_editor, exclude


included = (
    # 'id', 'title', 'project_link', 'participants_target', 'questionnaire', 'is_active',
    # 'markdown', 'creation_date', 'description', 'participants_count', 'project_img', 'tags'
    # 'members', 'members.user', 'members.user.fio', 'members.user.avatar', 'members.user.id'
)
excluded = (
    'members',
    'leaders.id', 'leaders.user.tags', 'leaders.user.as_leader', 'leaders.user.about', 'leaders.user.as_member'
)
PrivateProject = pydantic_model_creator(Project, exclude=excluded, include=included)
PublicProject = pydantic_model_creator(Project, exclude=excluded, include=included)
EditableProject = pydantic_model_creator(Project, exclude=(
    'id', 'is_active', 'members', 'leaders', 'creation_date', 'project_link', 'participants_count'
))
router = APIRouter()


class New(BaseModel):
    title: str = Field(max_length=128)
    description: str
    participants_target: int


# class Edit(BaseModel):
#     title: str = Field(max_length=128)
#     description: str
#     participants_target: int
#     questionnaire: str
#     markdown: str
#     description: str


async def project_by_link(project_link: str):
    return await instance_getter(Project, project_link=project_link)


@router.post('/create', response_model=PrivateProject)
async def create(new_project: New = Body(...), user: User = Depends(get_user)):
    project_link = await generate_link(Project)
    project = await Project.create(**new_project.dict(), project_link=project_link)
    await project.leaders.add(user)
    return await PrivateProject.from_tortoise_orm(project)


@router.put('/{project_link}/edit', response_model=PrivateProject)
async def edit(project: Project = Depends(project_by_link),
               user: User = Depends(get_user),
               edited: EditableProject = Body(...)):
    if await project.leaders.filter(user=user):
        project = await project.update_from_dict(exclude(edited.dict(), ['tags', ]))
        await m2m_editor(project.tags, [tag for tag in edited.dict()['tags']], Tag)
        await project.save()

        return await PrivateProject.from_tortoise_orm(project)
    raise HTTPException(403, 'Access denied')


@router.get('/all')
async def get():
    return await PrivateProject.from_queryset(Project.all())


@router.post('/{project_link}/enter', response_model=PublicProject)
async def enter(project_link: str, user: User = Depends(get_user)):
    project: Project = await project_by_link(project_link)
    await project.members.add(await user.as_member)
    return await PublicProject.from_tortoise_orm(project)


@router.get('/{project_link}/plus')
async def add_participant(project_link: str):
    project: Project = await project_by_link(project_link)
    project.participants_count += 1
    await project.save()
    return {'ok': True}


@router.get('/{project_link}', response_model=PublicProject)
async def show(project_link: str):
    project: Project = await project_by_link(project_link)
    return await PublicProject.from_tortoise_orm(project)


@router.get('/all')
async def get_all():
    return await PrivateProject.from_queryset(Project.all())
