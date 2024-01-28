from fastapi import APIRouter

router = APIRouter()


@router.get("/")
def read_root():
    return [
        {
            "id": 1,
            "name": "first"
        }
    ]

@router.get("/events_id")
def read_user(event_id: int):
    return {"event_id": event_id, "name": "first"}










