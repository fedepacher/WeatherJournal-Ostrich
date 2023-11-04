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


def get_tasks(user: user_schema.User):
    """Get all the user's entrance in the DB.

    Args:
        user (user_schema.User): User.

    Returns:
        list: List of entrance filtered by user.
    """
    tasks_by_user = WeatherModel.filter(
                                        WeatherModel.user_id == user.id
                                       ).order_by(WeatherModel.start_datetime.desc())

    tasks_list = []
    for task in tasks_by_user:
        tasks_list.append(weather_schema.Weather(
            id=task.id,
            city_name=task.city_name,
            start_datetime=task.start_datetime,
            end_datetime=task.end_datetime,
            avg_temperature=task.avg_temperature,
            latitude=task.latitude,
            longitude=task.longitude,
            comments=task.comments
        ))
    return tasks_list


def get_task_by_id(task_id: int, user: user_schema.User):
    """Get user's entrance by ID in the DB.

    Args:
        task_id (int): ID of the entrance.
        user (user_schema.User): User.

    Returns:
        weather_schema.Weather: Entrance fields schema.
    """
    tasks_by_id = WeatherModel.filter((WeatherModel.id == task_id) &
                                      (WeatherModel.user_id == user.id)
                                       ).first()

    if not tasks_by_id:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="ID not found"
        )

    return weather_schema.Weather(
        id=tasks_by_id.id,
        city_name=tasks_by_id.city_name,
        start_datetime=tasks_by_id.start_datetime,
        end_datetime=tasks_by_id.end_datetime,
        avg_temperature=tasks_by_id.avg_temperature,
        latitude=tasks_by_id.latitude,
        longitude=tasks_by_id.longitude,
        comments=tasks_by_id.comments
    )
