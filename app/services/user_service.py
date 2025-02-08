from datetime import datetime
from uuid import uuid4

from sqlalchemy.orm import Session

from app.db.models import User
from app.db.schemas import UserCreate, UserUpdate


class UserService:
    @staticmethod
    def create_user(db: Session, user_data: UserCreate):
        user = User(
            user_id=str(uuid4()),
            user_name=user_data.user_name,
            location_lat=user_data.location_lat,
            location_lon=user_data.location_lon,
            alert_threshold=user_data.alert_threshold,
            activity_tracking=user_data.activity_tracking,
            created_at=datetime.utcnow()
        )
        db.add(user)
        db.commit()
        db.refresh(user)
        return user

    @staticmethod
    def get_user_by_id(db: Session, user_id: str):
        return db.query(User).filter(User.user_id == user_id).first()

    @staticmethod
    def get_user_by_name(db: Session, user_name: str):
        return db.query(User).filter(User.user_name == user_name).first()

    @staticmethod
    def update_user(db: Session, user_id: str, user_data: UserUpdate):
        user = db.query(User).filter(User.user_id == user_id).first()
        if not user:
            return None
        for key, value in user_data.dict(exclude_unset=True).items():
            setattr(user, key, value)
        db.commit()
        db.refresh(user)
        return user

    @staticmethod
    def delete_user(db: Session, user_id: str):
        user = db.query(User).filter(User.user_id == user_id).first()
        if not user:
            return None
        db.delete(user)
        db.commit()
        return user
