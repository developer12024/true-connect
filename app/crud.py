from typing import List, Optional
from sqlmodel import select
from sqlalchemy.ext.asyncio import AsyncSession
from app.models import Profile
from app.schemas import ProfileCreate, ProfileUpdate

async def create_profile(session: AsyncSession, payload: ProfileCreate) -> Profile:
    profile = Profile(**payload.dict())
    session.add(profile)
    await session.commit()
    await session.refresh(profile)
    return profile

async def get_profile(session: AsyncSession, profile_id: int) -> Optional[Profile]:
    result = await session.get(Profile, profile_id)
    return result

async def list_profiles(session: AsyncSession, limit: int = 50, offset: int = 0) -> List[Profile]:
    q = select(Profile).offset(offset).limit(limit)
    result = await session.execute(q)
    return result.scalars().all()

async def update_profile(session: AsyncSession, profile_id: int, payload: ProfileUpdate) -> Optional[Profile]:
    profile = await get_profile(session, profile_id)
    if not profile:
        return None
    for k, v in payload.dict(exclude_unset=True).items():
        setattr(profile, k, v)
    session.add(profile)
    await session.commit()
    await session.refresh(profile)
    return profile

async def delete_profile(session: AsyncSession, profile_id: int) -> bool:
    profile = await get_profile(session, profile_id)
    if not profile:
        return False
    await session.delete(profile)
    await session.commit()
    return True