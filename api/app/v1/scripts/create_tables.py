from api.app.v1.model.user_model import Users
from api.app.v1.model.weather_model import Weather
from api.app.v1.utils.db import db


def create_tables():
    """Create DB tables."""
    with db:
        db.create_tables([Users, Weather])
