from fastapi import APIRouter
from fastapi import Depends
from fastapi import status
from fastapi import Body
from fastapi.security import OAuth2PasswordRequestForm

from api.app.v1.schema import user_schema
from api.app.v1.service import user_service
from api.app.v1.service import auth_service
from api.app.v1.schema.token_schema import Token
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


@router.post(
    "/login",
    tags=["users"],
    response_model=Token
)
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends()):
    """Login for access token.

    Args:
        form_data (OAuth2PasswordRequestForm, optional): Username/email or password. 
        Defaults to Depends().

    Returns:
        Token: Access token and token type.
    """
    access_token = auth_service.generate_token(form_data.username, form_data.password)
    return Token(access_token=access_token, token_type="bearer")
