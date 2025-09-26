from sqlmodel import SQLModel, create_engine
from sqlmodel.ext.asyncio.session import AsyncSession
from sqlalchemy.ext.asyncio import create_async_engine, AsyncEngine
from sqlalchemy.orm import sessionmaker
from app.core import settings

DATABASE_URL = settings.database_url

# async engine
engine: AsyncEngine = create_async_engine(DATABASE_URL, echo=False, future=True)
async_session = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)

async def init_db():
    # create tables (for simple development; production should use alembic migrations)
    async with engine.begin() as conn:
        await conn.run_sync(SQLModel.metadata.create_all)