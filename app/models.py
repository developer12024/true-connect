from sqlmodel import SQLModel, Field
from typing import Optional
from datetime import datetime

class SQLModelBase(SQLModel):
    pass

class Profile(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    full_name: str
    email: str = Field(index=True, unique=True)
    bio: Optional[str] = None
    created_at: datetime = Field(default_factory=datetime.utcnow)