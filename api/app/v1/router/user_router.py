from fastapi import APIRouter
from fastapi import Depends
from fastapi import status
from fastapi import Body

from api.app.v1.schema import user_schema
from api.app.v1.service import user_service
from api.app.v1.utils.db import get_db


router = APIRouter(
    prefix="/api/v1",
    tags=["users"]
)


@router.post(
    "/user/",
    status_code=status.HTTP_201_CREATED,
    response_model=user_schema.User,
    dependencies=[Depends(get_db)],
    summary="Create a new user"
)
def create_user(user: user_schema.UserRegister= Body(...)):
    """Create a new user in the app.

    Args:
        user (user_schema.UserRegister, optional): User params description. Defaults to Body(...).

    Returns:
        user: User info.
    """
    return user_service.create_user(user)
