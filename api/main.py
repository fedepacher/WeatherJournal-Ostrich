from fastapi import FastAPI

from api.app.v1.router.user_router import router as user_router
from api.app.v1.scripts.create_tables import create_tables

#create tables
create_tables()

app = FastAPI()

app.include_router(user_router)
