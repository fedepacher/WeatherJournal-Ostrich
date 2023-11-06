from datetime import datetime
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
def create_element(weather: weather_schema.Weather=Body(...),
                current_user: User =Depends(get_current_user)):
    """Create element in the DB.

    Args:
        weather (weather_schema.Weather): Element to be created.
        current_user (User, optional): Registered user. Defaults to Depends(get_current_user).

    Returns:
        json: Weather information created.
    """
    return weather_service.create_element(weather, current_user)


@router.get(
    "/",
    tags=["weather"],
    status_code=status.HTTP_200_OK,
    response_model=List[weather_schema.Weather],
    dependencies=[Depends(get_db)]
)
def get_elements(current_user: User = Depends(get_current_user)):
    """Get all DB elements.

    Args:
        current_user (User, optional): Registered user. Defaults to Depends(get_current_user).

    Returns:
        json: Weather information.
    """
    return weather_service.get_elements(current_user)


@router.get(
    "/{element_id}",
    tags=["weather"],
    status_code=status.HTTP_200_OK,
    response_model=weather_schema.Weather,
    dependencies=[Depends(get_db)]
)
def get_element(element_id: int = Path(..., gt=0),
                current_user: User = Depends(get_current_user)):
    """Get element by ID in the DB.

    Args:
        element_id (int): Id to find.
        current_user (User, optional): Registered user. Defaults to Depends(get_current_user).

    Returns:
        json: Weather information by ID.
    """
    return weather_service.get_element_by_id(element_id, current_user)


@router.patch(
    "/{element_id}",
    tags=["weather"],
    status_code=status.HTTP_200_OK,
    response_model=weather_schema.Weather,
    dependencies=[Depends(get_db)]
)
def update_element(element_id: int = Path(..., gt=0),
                   current_user: User = Depends(get_current_user),
                   city_name: str="",
                   start_datetime: datetime=None, end_datetime: datetime=None,
                   avg_temperature: float=None, latitude: float=None, longitude: float=None,
                   comments: str=""):
    """Update element fields by ID.

    Args:
        element_id (int, optional): Element ID. Defaults to Path(..., gt=0).
        current_user (User, optional): User. Defaults to Depends(get_current_user).
        city_name (str, optional): City ame. Defaults to "".
        start_datetime (datetime, optional): Start datetime. Defaults to None.
        end_datetime (datetime, optional): End datetime. Defaults to None.
        avg_temperature (float, optional): Average temperature. Defaults to None.
        latitude (float, optional): Latitude. Defaults to None.
        longitude (float, optional): Longitude. Defaults to None.
        comments (str, optional): Comments. Defaults to "".

    Returns:
        json: Weather information by ID.
    """
    return weather_service.update_element(element_id, current_user, city_name, start_datetime,
                                          end_datetime, avg_temperature, latitude, longitude,
                                          comments)


@router.delete(
    "/{element_id}",
    tags=["weather"],
    status_code=status.HTTP_200_OK,
    dependencies=[Depends(get_db)]
)
def delete_task(element_id: int = Path(..., gt=0), current_user: User = Depends(get_current_user)):
    """Delete element by ID.

    Args:
        element_id (int): Element ID.
        current_user (User, optional): User. Defaults to Depends(get_current_user).

    Returns:
        json: Deleted element's message.
    """
    weather_service.delete_element(element_id, current_user)

    return {'msg': f'Element {element_id} has been deleted successfully'}
