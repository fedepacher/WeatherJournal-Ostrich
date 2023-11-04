from datetime import datetime
from pydantic import BaseModel
from pydantic import Field


class CommentsCreate(BaseModel):
    comments: str = Field(
        ...,
        min_length=1,
        max_length=120,
        example="My comments"
    )


class Weather(CommentsCreate):
    id: int = Field(...)
    city_name: str = Field(default="")
    start_datetime: datetime = Field(default=datetime.now())
    end_datetime: datetime = Field(default=datetime.now())
    avg_temperature: float = Field(default=18.0)
    latitude: float = Field(default=0.0)
    longitude: float = Field(default=0.0)
