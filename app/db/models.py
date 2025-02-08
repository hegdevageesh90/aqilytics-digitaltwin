from sqlalchemy import Column, Integer, String, Float, DateTime, Boolean
from sqlalchemy.sql import func
from .database import Base


class User(Base):
    __tablename__ = 'users'

    user_id = Column(String, primary_key=True, index=True)
    user_name = Column(String)
    location_lat = Column(Float)
    location_lon = Column(Float)
    alert_threshold = Column(Integer)
    activity_tracking = Column(Boolean, default=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())


class AQIExposure(Base):
    __tablename__ = 'aqi_exposure'

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(String, index=True)
    aqi_value = Column(Float)
    location_lat = Column(Float)
    location_lon = Column(Float)
    timestamp = Column(DateTime(timezone=True), server_default=func.now())
