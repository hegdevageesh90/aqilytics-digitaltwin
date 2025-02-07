from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db.database import get_db
from app.services import aqi_service
from app.services.event_service import log_event

router = APIRouter()

@router.get("/aqi/{latitude}/{longitude}")
def get_aqi(latitude: float, longitude: float):
    aqi_value = aqi_service.fetch_aqi_data(latitude, longitude)
    return {"aqi": aqi_value}

@router.post("/events")
def log_aqi_event(user_id: str, latitude: float, longitude: float, db: Session = Depends(get_db)):
    aqi_value = aqi_service.fetch_aqi_data(latitude, longitude)
    event = log_event(db, user_id, "outdoor_activity", aqi_value, latitude, longitude)
    return event
