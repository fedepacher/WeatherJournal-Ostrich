from fastapi import FastAPI

from api.app.v1.router.user_router import router as user_router
from api.app.v1.router.weather_router import router as weather_router
from api.app.v1.router.forecast_router import router as forecast_router
from api.app.v1.scripts.create_tables import create_tables

#create tables
create_tables()

app = FastAPI()

app.include_router(user_router)
app.include_router(weather_router)
app.include_router(forecast_router)
