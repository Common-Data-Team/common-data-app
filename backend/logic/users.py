from fastapi import APIRouter, HTTPException, Depends, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from tortoise.contrib.pydantic import pydantic_model_creator
from models import User, Member, Leader, Tag
from typing import Union, Optional, List, Any
from datetime import timedelta, datetime
from passlib.context import CryptContext
from jose import JWTError, jwt

from settings import ALGORITHM, ACCESS_TOKEN_EXPIRE_MINUTES, SECRET_KEY
from pydantic import BaseModel

router = APIRouter()
pwd_context = CryptContext(schemes=['bcrypt'], deprecated='auto')
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/users/token")

included = (
    'fio', 'email', 'level', 'avatar', 'about', 'tags', 'tags.name',
    'as_leader', 'as_leader.projects', 'as_leader.projects.project_link', 'as_leader.projects.title',
    'as_leader.projects.participants_count', 'as_leader.projects.participants_target', 'as_leader.projects.project_img',
    'as_leader.projects.tags', 'as_leader.projects.tags.name',

    # 'as_member', 'as_member.projects', 'as_member.projects.project_link', 'as_member.projects.title'
)

excluded = (

)

PublicUser = pydantic_model_creator(User, name='PublicUser', include=included)
PrivateUser = pydantic_model_creator(User, name='PrivateUser', include=included)


class Token(BaseModel):
    access_token: str
    token_type: str
    user_id: int


class PublicHash(BaseModel):
    hash: str


class Success(BaseModel):
    ok: bool
    payload: Optional[Any] = None


async def authenticate_user(username: str, password: str) -> Union[User, None]:
    user = await User.get_or_none(email=username)
    if user is None:
        return None
    if not pwd_context.verify(password, user.hashed_password):
        return None
    return user


async def get_user(token: str = Depends(oauth2_scheme)) -> User:
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )

    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get('sub')
        if username is None:
            raise credentials_exception
    except JWTError:
        raise credentials_exception

    user = await User.get_or_none(email=username)
    if user is None:
        raise credentials_exception
    return user


async def get_admin(user: User = Depends(get_user)):
    if user.is_admin:
        return user
    raise HTTPException(status_code=403, detail='Forbidden')


def create_access_token(data, expires_data: Optional[timedelta] = None):
    to_encode = data.copy()
    if expires_data is not None:
        expire = datetime.utcnow() + expires_data
    else:
        expire = datetime.utcnow() + timedelta(minutes=30)
    to_encode.update({'exp': expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, ALGORITHM)
    return encoded_jwt


async def create_user_and_token(email, password):
    user = await User.create(email=email, hashed_password=pwd_context.hash(password))
    await Member.create(user=user)
    await Leader.create(user=user)
    expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    return user, create_access_token(data={'sub': user.email}, expires_data=expires)


@router.post('/token', response_model=Token)
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends()):
    user = await authenticate_user(form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(data={'sub': user.email}, expires_data=expires)
    return Token(access_token=access_token, token_type='bearer', user_id=user.id)


@router.post('/create', response_model=Token)
async def new_user(form_data: OAuth2PasswordRequestForm = Depends()):
    user = await User.get_or_none(email=form_data.username)
    if user is not None:
        raise HTTPException(400, 'User already exists')
    user, token = await create_user_and_token(form_data.username, form_data.password)
    return Token(access_token=token, token_type='bearer', user_id=user.id)


@router.get('/profile', response_model=PrivateUser)
async def profile(user: User = Depends(get_user)):
    return await PrivateUser.from_tortoise_orm(user)


class Edit(BaseModel):
    fio: str
    tags: List[str]
    about: str


@router.put('/edit', response_model=PrivateUser)
async def edit(edited: Edit, user=Depends(get_user)):
    user = await user.update_from_dict(dict(fio=edited.fio, about=edited.about))
    user_tags = set(await user.tags.all())
    if len(user_tags) > 0:
        await user.tags.remove(*user_tags)

    for tag in edited.tags:
        tag_instance = await Tag.get_or_none(name=tag)
        if tag_instance is not None:
            await user.tags.add(tag_instance)
    await user.save()
    return await PrivateUser.from_tortoise_orm(user)


@router.delete('/delete')
async def destroy(user=Depends(get_user)):
    await user.delete()
    return {'ok': True}


@router.get('/{user_id}', response_model=PublicUser)
async def user_by_id(user_id: int):
    user = await User.get_or_none(id=user_id)
    if user:
        return await PublicUser.from_tortoise_orm(user)
    raise HTTPException(404, 'User not found')


@router.get('/all')
async def all_users():
    return await PrivateUser.from_queryset(User.all())
