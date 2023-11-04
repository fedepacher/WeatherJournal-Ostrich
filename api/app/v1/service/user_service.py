from fastapi import HTTPException, status

from passlib.context import CryptContext

from api.app.v1.model.user_model import Users as UserModel
from api.app.v1.schema import user_schema


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def get_password_hash(password):
    return pwd_context.hash(password)

def create_user(user: user_schema.UserRegister):
    """Create users and store them in the DB.

    Args:
        user (user_schema.UserRegister): User parameters.

    Raises:
        HTTPException: If the user is already created.

    Returns:
        user_schema.User: User schema.
    """
    get_user = UserModel.filter((UserModel.email == user.email) 
                                | (UserModel.username == user.username)).first()
    if get_user:
        msg = "Email already registered"
        if get_user.username == user.username:
            msg = "Username already registered"
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=msg
        )

    db_user = UserModel(
        username=user.username,
        email=user.email,
        password=get_password_hash(user.password)
    )

    db_user.save()

    return user_schema.User(
        id = db_user.id,
        username = db_user.username,
        email = db_user.email
    )
