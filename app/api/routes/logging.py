from fastapi import APIRouter, Depends

from app.api.dependencies.authentication import get_current_user_authorizer
from app.core.config import get_app_settings
from app.core.settings.app import AppSettings
from app.models.domain.users import User
from app.models.schemas.users import OnlyCTFResponse
from app.resources import strings
from app.services import jwt

router = APIRouter()


@router.get("", response_model=OnlyCTFResponse, name="logging:get-logging-page", include_in_schema=False)
async def retrieve_logging_page(
        user: User = Depends(get_current_user_authorizer()),
        settings: AppSettings = Depends(get_app_settings),
) -> OnlyCTFResponse:
    token = jwt.create_access_token_for_user(
        user,
        str(settings.secret_key.get_secret_value()),
    )
    return OnlyCTFResponse(
        flag=strings.InsufficientLogging(),
        description=strings.DescriptionInsufficientLogging,
    )
