from typing import Optional

from pydantic import BaseModel, EmailStr, HttpUrl

from app.models.domain.users import User
from app.models.schemas.rwschema import RWSchema


class UserInLogin(RWSchema):
    email: EmailStr
    password: str


class UserInCreate(UserInLogin):
    username: str


class UserInUpdate(BaseModel):
    username: Optional[str] = None
    email: Optional[EmailStr] = None
    password: Optional[str] = None
    bio: Optional[str] = None
    image: Optional[HttpUrl] = None
    admin: Optional[bool] = None


class UserWithToken(User):
    token: str


class UserInResponse(RWSchema):
    user: UserWithToken


class CTFResponse(UserInResponse):
    flag: str
    description: str


class OnlyCTFResponse(BaseModel):
    flag: str
    description: str


class OnlyCTFResponseWithSecret(BaseModel):
    flag: str
    description: str
    secret: str
