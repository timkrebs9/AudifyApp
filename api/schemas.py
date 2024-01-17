from pydantic import EmailStr
from pydantic_settings import BaseSettings
from datetime import datetime
from typing import Optional

from pydantic.types import conint


class PostBase(BaseSettings):
    title: str
    content: str
    published: bool = True


class PostCreate(PostBase):
    pass


class UserOut(BaseSettings):
    id: int
    email: EmailStr
    created_at: datetime

    class Config:
        orm_mode = True


class Post(PostBase):
    id: int
    created_at: datetime
    owner_id: int
    owner: UserOut

    class Config:
        orm_mode = True


class PostOut(BaseSettings):
    Post: Post
    votes: int

    class Config:
        orm_mode = True


class UserCreate(BaseSettings):
    email: EmailStr
    password: str


class UserLogin(BaseSettings):
    email: EmailStr
    password: str


class Token(BaseSettings):
    access_token: str
    token_type: str


class TokenData(BaseSettings):
    id: Optional[str] = None


class Vote(BaseSettings):
    post_id: int
    dir: conint(le=1)
