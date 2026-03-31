from datetime import datetime
from typing import Optional, Annotated
from pydantic import BaseModel, ConfigDict, EmailStr, Field
from pydantic import conint


class PostBase(BaseModel):
    title: str
    content: str
    published: bool = True

    model_config = ConfigDict(from_attributes=True)


class PostCreate(PostBase):
    pass


class UserResponse(BaseModel):
    id: int
    email: str
    created_at: datetime


class PostUpdate(BaseModel):
    title: Optional[str] = None
    content: Optional[str] = None
    published: Optional[bool] = None

    model_config = ConfigDict(from_attributes=True)

class Post(PostBase):
    id: int
    created_at: datetime
    owner_id: int
    owner: UserResponse

class PostResponse(Post):

    model_config = ConfigDict(from_attributes=True)


class UserCreate(BaseModel):
    email: EmailStr
    password: str = Field(min_length=8, max_length=72)


class UserLogin(BaseModel):
    email: EmailStr
    password: str

class TokenData(BaseModel):
    id: Optional[int] = None

VoteDir = Annotated[int, Field(ge=0, le=1)]

class Vote(BaseModel):
    post_id: int
    dir: VoteDir