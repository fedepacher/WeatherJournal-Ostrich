from fastapi import APIRouter, status, Depends

from api.app.v1.service import forecast_service
from api.app.v1.utils.db import get_db
from api.app.v1.schema.user_schema import User
from api.app.v1.service.auth_service import get_current_user



router = APIRouter(prefix="/api/v1/forecast")


@router.get(
    "/{city_name}",
    tags=["forecast"],
    status_code=status.HTTP_200_OK,
    dependencies=[Depends(get_db)]
)
def get_forecast_by_city_name(city_name: str, current_user: User = Depends(get_current_user)):
    """Get forecast by city name.

    Args:
        city_name (str): City name.
        current_user (User, optional): User. Defaults to Depends(get_current_user).

    Returns:
        JSON: Json API response
    """
    return forecast_service.get_forecast_by_city(city_name, current_user)


@router.post(
    "/{latitude}&{longitude}",
    tags=["forecast"],
    status_code=status.HTTP_200_OK,
    dependencies=[Depends(get_db)]
)
def get_forecast_by_lat_lon(latitude: float, longitude: float, 
                            current_user: User = Depends(get_current_user)):
    """Get forecast by latitud and longitude.

    Args:
        latitude (float): Latitude.
        longitude (float): Longitude.
        current_user (User, optional): User. Defaults to Depends(get_current_user).

    Returns:
        JSON: Json API response
    """
    return forecast_service.get_forecast_by_lat_lon(latitude, longitude, current_user)
