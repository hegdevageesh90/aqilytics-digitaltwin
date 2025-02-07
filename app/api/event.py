from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.core.logger import get_logger
from app.db.database import get_db
from app.services.event_service import log_event

router = APIRouter()
logger = get_logger()


@router.post("/log_event/")
async def log_aqi_exposure_event(user_id: str, aqi_value: float, latitude: float, longitude: float,
                                 db: Session = Depends(get_db)):
    try:
        logger.info(f"Received event log request from user {user_id} for AQI exposure.")
        event = log_event(db=db, user_id=user_id, event_type="exposure", aqi_value=aqi_value,
                          location_lat=latitude, location_lon=longitude)
        logger.info(f"Event logged successfully with ID {event.id}.")
        return {"message": "Event logged successfully", "event_id": event.id}
    except Exception as e:
        logger.error(f"Error logging event for user {user_id}: {str(e)}")
        raise HTTPException(status_code=500, detail="Failed to log event")
