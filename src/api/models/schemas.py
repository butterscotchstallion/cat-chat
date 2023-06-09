from pydantic import BaseModel
from datetime import datetime
from typing import Optional


class UserBase(BaseModel):
    username: str
    password: str
    guid: Optional[str]
    avatar_filename: Optional[str]
    created_at: Optional[datetime] = datetime.now()
    updated_at: Optional[datetime] = datetime.now()
    active: Optional[bool] = True

    class Config:
        orm_mode = True


class UserCreate(UserBase):
    password: str


class UserAuth(BaseModel):
    username: str
    password: str
