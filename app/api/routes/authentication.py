from typing import Union

from fastapi import APIRouter, Body, Depends, HTTPException
from starlette.status import HTTP_201_CREATED, HTTP_400_BAD_REQUEST

from app.api.dependencies.database import get_repository
from app.core.config import get_app_settings
from app.core.settings.app import AppSettings
from app.db.errors import EntityDoesNotExist
from app.db.repositories.users import UsersRepository
from app.models.schemas.users import (
    UserInLogin,
    UserInResponse,
    UserWithToken, OnlyCTFResponse, OnlyCTFResponseWithSecret, CTFResponse
)
from app.resources import strings
from app.services import jwt

router = APIRouter()


@router.post("/login", response_model=Union[CTFResponse, UserInResponse] , name="auth:login")
async def login(
    user_login: UserInLogin = Body(..., embed=True, alias="user"),
    users_repo: UsersRepository = Depends(get_repository(UsersRepository)),
    settings: AppSettings = Depends(get_app_settings),
) -> Union[CTFResponse, UserInResponse]:
    wrong_login_error = HTTPException(
        status_code=HTTP_400_BAD_REQUEST,
        detail=strings.INCORRECT_LOGIN_INPUT,
    )

    try:
        user = await users_repo.get_user_by_email(email=user_login.email)
    except EntityDoesNotExist as existence_error:
        raise wrong_login_error from existence_error

    if not user.check_password(user_login.password):
        raise wrong_login_error

    token = jwt.create_access_token_for_user(
        user,
        str(settings.secret_key.get_secret_value()),
    )
    if user_login.email == "Pikachu@checkmarx.com":
        return CTFResponse(
        flag=strings.BrokenUserAuthentication(),
        description=strings.DescriptionBrokenUserAuthentication,
        user=UserWithToken(
            username=user.username,
            email=user.email,
            image=user.image,
            token=token,
            bio="THIS IS A TOP SECRET: This application is not logging and monitoring user's activities... You might wanna check the logging endpoint in the application.."
        ),
    )

    else:
        return UserInResponse(
            user=UserWithToken(
                username=user.username,
                email=user.email,
                bio=user.bio,
                image=user.image,
                token=token,
                admin=user.admin
            ),
        )
