from typing import List, Optional

from pydantic import BaseModel

from models.core import Event

class EventBase(BaseModel):
    hobby: str
    description: Optional[str] = None

class EventCreate(EventBase):
    pass

class Event(EventBase):
    id: int
    owner_id: int

class Config:
    orm_mode = True
class UserBase(BaseModel):
    email: str

class UserCreate(UserBase):
    password: str

class User(UserBase):
    id: int
    is_active: bool
    events: List[Event] = []


class Config:
    orm_mode = True





