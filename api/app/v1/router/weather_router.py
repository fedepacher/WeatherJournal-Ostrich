from fastapi import APIRouter, Depends, Body, status, Query, Path
from typing import List, Optional

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


@router.get(
    "/",
    tags=["weather"],
    status_code=status.HTTP_200_OK,
    response_model=List[weather_schema.Weather],
    dependencies=[Depends(get_db)]
)
def get_tasks(current_user: User = Depends(get_current_user)):
    return weather_service.get_tasks(current_user)


@router.get(
    "/{task_id}",
    tags=["weather"],
    status_code=status.HTTP_200_OK,
    response_model=weather_schema.Weather,
    dependencies=[Depends(get_db)]
)
def get_task(task_id: int = Path(..., gt=0),
             current_user: User = Depends(get_current_user)
):
    return weather_service.get_task_by_id(task_id, current_user)
