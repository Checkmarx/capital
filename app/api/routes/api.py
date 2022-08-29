from fastapi import APIRouter

from app.api.routes import authentication, comments, profiles, tags, users, admin, authentication_old, debug, register,\
    membership, logging
from app.api.routes.articles import api as articles

router = APIRouter()
router.include_router(register.router, tags=["authentication"], prefix="/users")
router.include_router(authentication.router, tags=["authentication"], prefix="/v2/users")
router.include_router(authentication_old.router, tags=["authentication"], prefix="/v1/users")
router.include_router(users.router, tags=["users"], prefix="/user")
router.include_router(membership.router, tags=["membership"], prefix="/membership")
router.include_router(admin.router, tags=["admin"], prefix="/admin")
router.include_router(logging.router, tags=["logging"], prefix="/logging")
router.include_router(profiles.router, tags=["profiles"], prefix="/profiles")
router.include_router(articles.router, tags=["articles"])
router.include_router(debug.router, tags=["debug"], prefix="/debug")
router.include_router(
    comments.router,
    tags=["comments"],
    prefix="/articles/{slug}/comments",
)
router.include_router(tags.router, tags=["tags"], prefix="/tags")
