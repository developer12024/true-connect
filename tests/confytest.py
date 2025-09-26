import asyncio
import pytest
from httpx import AsyncClient
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlmodel import SQLModel
from app.main import app
from app.db import engine
from app.core import settings

TEST_DATABASE_URL = settings.database_url.replace('trueconnect_db', 'trueconnect_test_db')

@pytest.fixture(scope="session")
def anyio_backend():
    return 'asyncio'

@pytest.fixture(scope="session")
async def initialize_db():
    # create test database tables (uses same DB server; in CI recommend a separate ephemeral DB)
    test_engine = create_async_engine(TEST_DATABASE_URL, future=True)
    async with test_engine.begin() as conn:
        await conn.run_sync(SQLModel.metadata.create_all)
    yield
    async with test_engine.begin() as conn:
        await conn.run_sync(SQLModel.metadata.drop_all)

@pytest.fixture
async def client(initialize_db):
    async with AsyncClient(app=app, base_url="http://testserver") as ac:
        yield ac