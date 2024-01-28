from typing import Union
from models import core
from models.database import engine
from fastapi import FastAPI
from routers.events import router as event_router
from routers.users import router as users_router

core.Base.metadata.create_all(bind=engine)

app = FastAPI()


app.include_router(
    router=event_router,
    prefix='/events'
)

app.include_router(
    router=users_router,
    prefix='/users'
)