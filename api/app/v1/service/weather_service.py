from fastapi import HTTPException, status

from api.app.v1.schema import weather_schema
from api.app.v1.schema import user_schema
from api.app.v1.model.weather_model import Weather as WeatherModel


def create_task(task: weather_schema.Weather, user: user_schema.User):
    """Create a new entrance in the database.

    Args:
        task (weather_schema.CommentsCreate): Entrance to add to the DB.
        user (user_schema.User): User.

    Returns:
        weather_schema.Weather: Entrance fields schema.
    """
    db_task = WeatherModel(
        city_name=task.city_name,
        start_datetime=task.start_datetime,
        end_datetime=task.end_datetime,
        avg_temperature=task.avg_temperature,
        latitude=task.latitude,
        longitude=task.longitude,
        comments=task.comments,
        user_id=user.id
    )

    db_task.save()

    return weather_schema.Weather(
        id=db_task.id,
        city_name=db_task.city_name,
        start_datetime=db_task.start_datetime,
        end_datetime=db_task.end_datetime,
        avg_temperature=db_task.avg_temperature,
        latitude=db_task.latitude,
        longitude=db_task.longitude,
        comments=db_task.comments
    )
