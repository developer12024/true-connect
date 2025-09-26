from fastapi import APIRouter, Depends, HTTPException, status
from typing import List
from sqlmodel.ext.asyncio.session import AsyncSession
from app.db import async_session
from app import crud, schemas

router = APIRouter(prefix="/profiles", tags=["profiles"])

async def get_session():
    async with async_session() as session:
        yield session

@router.post("/", response_model=schemas.ProfileRead, status_code=status.HTTP_201_CREATED)
async def create_profile(payload: schemas.ProfileCreate, session: AsyncSession = Depends(get_session)):
    created = await crud.create_profile(session, payload)
    return created

@router.get("/", response_model=List[schemas.ProfileRead])
async def list_profiles(limit: int = 50, offset: int = 0, session: AsyncSession = Depends(get_session)):
    return await crud.list_profiles(session, limit=limit, offset=offset)

@router.get("/{profile_id}", response_model=schemas.ProfileRead)
async def read_profile(profile_id: int, session: AsyncSession = Depends(get_session)):
    profile = await crud.get_profile(session, profile_id)
    if not profile:
        raise HTTPException(status_code=404, detail="Profile not found")
    return profile

@router.patch("/{profile_id}", response_model=schemas.ProfileRead)
async def update_profile(profile_id: int, payload: schemas.ProfileUpdate, session: AsyncSession = Depends(get_session)):
    profile = await crud.update_profile(session, profile_id, payload)
    if not profile:
        raise HTTPException(status_code=404, detail="Profile not found")
    return profile

@router.delete("/{profile_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_profile(profile_id: int, session: AsyncSession = Depends(get_session)):
    ok = await crud.delete_profile(session, profile_id)
    if not ok:
        raise HTTPException(status_code=404, detail="Profile not found")
    return None