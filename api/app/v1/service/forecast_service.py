import requests

from fastapi import HTTPException, status

from api.app.v1.utils.settings import Settings
from api.app.v1.schema import user_schema


settings = Settings()
API_KEY = settings.forecast_api_key


def get_forecast_by_city(city_name: str, user: user_schema.User):
    """Get forecast by city name.

    Args:
        city_name (str): City name.
        current_user (User, optional): User. Defaults to Depends(get_current_user).

    Returns:
        JSON: Json API response
    """
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&APPID={API_KEY}"

    response = requests.get(url)

    return response.json()


def get_forecast_by_lat_lon(latitude: float, longitude: float, user: user_schema.User):
    """Get forecast by latitud and longitude.

    Args:
        latitude (float): Latitude.
        longitude (float): Longitude.
        current_user (User, optional): User. Defaults to Depends(get_current_user).

    Returns:
        json: Json API response
    """
    url = f"https://api.openweathermap.org/data/2.5/weather?lat={latitude}&lon={longitude}" \
          f"&APPID={API_KEY}"
    response = requests.get(url)

    return response.json()
