from fastapi import APIRouter, Depends
from pydantic import BaseModel

from app.api.dependencies.authentication import get_current_user_authorizer

from app.models.domain.users import User
from app.resources.strings import ExcessiveDataExposure, DescriptionExcessiveDataExposure

router = APIRouter()


class Member(BaseModel):
    number: str
    cvc: str
    expiry: str
    name: str


@router.post("", name="Membership:Subscribe")
async def membership(
        member: Member,
        user: User = Depends(get_current_user_authorizer()),

):
    if (
            member.number == '4426111122223333' and
            member.cvc == '555' and
            member.name == 'Team Rocket' and
            member.expiry == '0922'
    ):
        return "{}\n\n{}".format(ExcessiveDataExposure(), DescriptionExcessiveDataExposure)
    else:
        return "Card declined, try again!"
