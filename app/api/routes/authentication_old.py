from fastapi import APIRouter, Body, Depends, HTTPException
from starlette.status import HTTP_400_BAD_REQUEST

from app.resources.strings import ImproperAssetsManagement, DescriptionImproperAssetsManagement
from app.api.dependencies.database import get_repository
from app.db.errors import EntityDoesNotExist
from app.db.repositories.users import UsersRepository
from app.models.schemas.users import (
    UserInLogin,
    UserWithToken, CTFResponse,
)
from app.resources import strings

router = APIRouter()


@router.post("/login", response_model=CTFResponse, name="auth:login", include_in_schema=False)
async def login(
    user_login: UserInLogin = Body(..., embed=True, alias="user"),
    users_repo: UsersRepository = Depends(get_repository(UsersRepository)),
) -> CTFResponse:
    wrong_login_error = HTTPException(
        status_code=HTTP_400_BAD_REQUEST,
        detail=strings.INCORRECT_LOGIN_INPUT,
    )

    try:
        user = await users_repo.get_user_by_email(email=user_login.email)
    except EntityDoesNotExist as existence_error:
        raise wrong_login_error from existence_error

    return CTFResponse(
        flag=ImproperAssetsManagement(),
        description=DescriptionImproperAssetsManagement,
        user=UserWithToken(
            username=user.username,
            email=user.email,
            image=user.image,
            token="Keep it up!",
            bio=user.bio,
        ),
    )

