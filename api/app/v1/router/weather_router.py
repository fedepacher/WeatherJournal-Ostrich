from fastapi import APIRouter, Depends, Body
from fastapi import status

from api.app.v1.schema import weather_schema
from api.app.v1.service import weather_service
from api.app.v1.utils.db import get_db
from api.app.v1.schema.user_schema import User
from api.app.v1.service.auth_service import get_current_user


router = APIRouter(prefix="/api/v1/weather")

@router.post(
    "/",
    tags=["weather"],
    status_code=status.HTTP_201_CREATED,
    response_model=weather_schema.Weather,
    dependencies=[Depends(get_db)]
)
def create_task(weather: weather_schema.Weather=Body(...),
                current_user: User =Depends(get_current_user)):
    return weather_service.create_task(weather, current_user)
