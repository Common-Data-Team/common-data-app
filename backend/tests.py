import asyncio
import pytest
import warnings
import shutil
import json
from typing import Generator
from tortoise.contrib.test import finalizer, initializer
from tortoise.contrib.fastapi import register_tortoise
from logic.tools import random_string
from fastapi.testclient import TestClient
from contextvars import ContextVar
from settings import TORTOISE_ORM
from app import app

token_cxt: ContextVar[str] = ContextVar('token')


@pytest.fixture(scope='module')
def client() -> Generator:
    initializer(['models'])
    with TestClient(app) as c:
        yield c
    finalizer()


@pytest.fixture(scope='module')
def event_loop(client: TestClient) -> Generator:
    yield client.task.get_loop()


# def test_create_user():
def test_create_user(client: TestClient, event_loop: asyncio.AbstractEventLoop):
    randomized = random_string(6)
    response = client.post('/users/create', data=dict(username=randomized, password=randomized))
    assert response.status_code == 200
    token_cxt.set(response.json()['access_token'])


def test_edit_user(client: TestClient, event_loop: asyncio.AbstractEventLoop):
    response = client.put('users/edit', )


def test_project_creation(client: TestClient, event_loop: asyncio.AbstractEventLoop):
    response = client.post(
        '/projects/create',
        headers=dict(Authorization=f'Bearer {token_cxt.get()}'),
        data=json.dumps(dict(
            title="New project",
            description="Description",
            participants_target=500
        )))
    assert response.status_code == 200
