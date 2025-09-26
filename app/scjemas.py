from pydantic import BaseModel, EmailStr
from typing import Optional

class ProfileCreate(BaseModel):
    full_name: str
    email: EmailStr
    bio: Optional[str] = None

class ProfileRead(ProfileCreate):
    id: int
    created_at: Optional[str]

class ProfileUpdate(BaseModel):
    full_name: Optional[str]
    email: Optional[EmailStr]
    bio: Optional[str]