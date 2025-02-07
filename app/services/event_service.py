import datetime

from sqlalchemy.orm import Session

from app.core.logger import get_logger
from app.db import models

logger = get_logger()


def log_event(db: Session, user_id: str, event_type: str, aqi_value: float, location_lat: float, location_lon: float):
    try:
        logger.info(f"Logging event for user {user_id}: {event_type}, AQI: {aqi_value}")
        new_event = models.AQIExposure(
            user_id=user_id,
            aqi_value=aqi_value,
            location_lat=location_lat,
            location_lon=location_lon,
            timestamp=datetime.datetime.now()
        )
        db.add(new_event)
        db.commit()
        db.refresh(new_event)
        logger.info(f"Event logged successfully: {new_event.id}")
        return new_event
    except Exception as e:
        logger.error(f"Failed to log event for user {user_id}: {str(e)}")
        raise e
