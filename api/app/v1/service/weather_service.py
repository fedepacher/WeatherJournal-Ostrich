from fastapi import HTTPException, status
from datetime import datetime

from api.app.v1.schema import weather_schema
from api.app.v1.schema import user_schema
from api.app.v1.model.weather_model import Weather as WeatherModel


def create_element(element: weather_schema.Weather, user: user_schema.User):
    """Create a new entrance in the database.

    Args:
        element (weather_schema.CommentsCreate): Entrance to add to the DB.
        user (user_schema.User): User.

    Returns:
        weather_schema.Weather: Entrance fields schema.
    """
    db_element = WeatherModel(
        city_name=element.city_name,
        start_datetime=element.start_datetime,
        end_datetime=element.end_datetime,
        avg_temperature=element.avg_temperature,
        latitude=element.latitude,
        longitude=element.longitude,
        comments=element.comments,
        user_id=user.id
    )

    db_element.save()

    return weather_schema.Weather(
        id=db_element.id,
        city_name=db_element.city_name,
        start_datetime=db_element.start_datetime,
        end_datetime=db_element.end_datetime,
        avg_temperature=db_element.avg_temperature,
        latitude=db_element.latitude,
        longitude=db_element.longitude,
        comments=db_element.comments
    )


def get_elements(user: user_schema.User):
    """Get all the user's entrance in the DB.

    Args:
        user (user_schema.User): User.

    Returns:
        list: List of entrance filtered by user.
    """
    elements_by_user = WeatherModel.filter(
                                        WeatherModel.user_id == user.id
                                       ).order_by(WeatherModel.start_datetime.desc())

    elements_list = []
    for element in elements_by_user:
        elements_list.append(weather_schema.Weather(
            id=element.id,
            city_name=element.city_name,
            start_datetime=element.start_datetime,
            end_datetime=element.end_datetime,
            avg_temperature=element.avg_temperature,
            latitude=element.latitude,
            longitude=element.longitude,
            comments=element.comments
        ))
    return elements_list


def get_element_by_id(element_id: int, user: user_schema.User):
    """Get user's entrance by ID in the DB.

    Args:
        element_id (int): ID of the entrance.
        user (user_schema.User): User.

    Returns:
        weather_schema.Weather: Entrance fields schema.
    """
    elements_by_id = WeatherModel.filter((WeatherModel.id == element_id) &
                                         (WeatherModel.user_id == user.id)
                                        ).first()

    if not elements_by_id:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f'Element {element_id} not found'
        )

    return weather_schema.Weather(
        id=elements_by_id.id,
        city_name=elements_by_id.city_name,
        start_datetime=elements_by_id.start_datetime,
        end_datetime=elements_by_id.end_datetime,
        avg_temperature=elements_by_id.avg_temperature,
        latitude=elements_by_id.latitude,
        longitude=elements_by_id.longitude,
        comments=elements_by_id.comments
    )


def update_element(element_id: int, user: user_schema.User, city_name: str="",
                   start_datetime: datetime=None, end_datetime: datetime=None,
                   avg_temperature: float=None, latitude: float=None, longitude: float=None,
                   comments: str=""):
    """Upadte element by ID.

    Args:
        element_id (int): Element ID.
        user (user_schema.User): User.
        city_name (str, optional): City's name. Defaults to "".
        start_datetime (datetime, optional): Start datetime. Defaults to None.
        end_datetime (datetime, optional): End datetime. Defaults to None.
        avg_temperature (float, optional): Average temperature. Defaults to None.
        latitude (float, optional): Latitude. Defaults to None.
        longitude (float, optional): Longiture. Defaults to None.

    Raises:
        HTTPException: If element was not found.

    Returns:
        weather_schema.Weather: Updated entrance fields schema.
    """
    element = WeatherModel.filter((WeatherModel.id == element_id) &
                                  (WeatherModel.user_id == user.id)).first()

    if not element:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Element not found"
        )

    if city_name != "":
        element.city_name = city_name
    if start_datetime is not None:
        element.start_datetime = start_datetime
    if end_datetime is not None:
        element.end_datetime = end_datetime
    if avg_temperature is not None:
        element.avg_temperature = avg_temperature
    if latitude is not None:
        element.start_datetime = latitude
    if longitude is not None:
        element.start_datetime = longitude
    if comments != "":
        element.comments = comments

    element.save()

    return weather_schema.Weather(
        id=element.id,
        city_name=element.city_name,
        start_datetime=element.start_datetime,
        end_datetime=element.end_datetime,
        avg_temperature=element.avg_temperature,
        latitude=element.latitude,
        longitude=element.longitude,
        comments=element.comments
    )


def delete_element(element_id: int, user: user_schema.User):
    """Delete element by ID

    Args:
        element_id (int): Element ID.
        user (user_schema.User): User.

    Raises:
        HTTPException: If element was not found.
    """
    element = WeatherModel.filter((WeatherModel.id == element_id) &
                                  (WeatherModel.user_id == user.id)).first()
    if not element:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f'Element {element_id} not found'
        )

    element.delete_instance()
