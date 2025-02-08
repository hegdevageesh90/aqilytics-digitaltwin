from pydantic import BaseModel
from typing import Optional
from datetime import datetime


class UserBase(BaseModel):
    user_name: str
    location_lat: float
    location_lon: float
    alert_threshold: int
    activity_tracking: bool = True


class UserCreate(UserBase):
    pass


class UserUpdate(UserBase):
    location_lat: Optional[float] = None
    location_lon: Optional[float] = None
    alert_threshold: Optional[int] = None
    activity_tracking: Optional[bool] = None


class UserResponse(UserBase):
    user_id: str
    created_at: datetime

    class Config:
        orm_mode = True
