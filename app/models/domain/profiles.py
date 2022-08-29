from typing import Optional

from app.models.domain.rwmodel import RWModel


class Profile(RWModel):
    admin: bool = False
    username: str
    bio: str = ""
    image: Optional[str] = None
    following: bool = False
    card_name: Optional[str]
    card_number: Optional[str]
    card_cvc: Optional[str]
    card_expiry: Optional[str]
