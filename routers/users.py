from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from controllers.users import get_users
from models import shemas
from models.database import get_db

# from models.database import get_db
router = APIRouter()

@router.get("/", response_model=List[shemas.User])
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = get_users(db, skip=skip, limit=limit)