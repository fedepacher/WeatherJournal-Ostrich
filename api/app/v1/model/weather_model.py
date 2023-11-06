import peewee
from datetime import datetime

from api.app.v1.utils.db import db
from .user_model import Users


class Weather(peewee.Model):
    """DB weather columns definition.

    Args:
        peewee (_type_): Validation model.
    """
    city_name = peewee.CharField()
    start_datetime = peewee.DateTimeField(default=datetime.now)
    end_datetime = peewee.DateTimeField(default=datetime.now)
    avg_temperature = peewee.FloatField()
    latitude = peewee.FloatField()
    longitude = peewee.FloatField()
    comments = peewee.CharField()
    user = peewee.ForeignKeyField(Users, backref='weather')

    class Meta:
        """DB connection"""
        database = db
