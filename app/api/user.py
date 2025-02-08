from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.database import get_db
from app.db.schemas import UserCreate, UserResponse, UserUpdate
from app.services.user_service import UserService

router = APIRouter()


@router.post("/users", response_model=UserResponse)
def create_user(user_data: UserCreate, db: Session = Depends(get_db)):
    return UserService.create_user(db, user_data)


@router.get("/users/id/{user_id}", response_model=UserResponse)
def get_user(user_id: str, db: Session = Depends(get_db)):
    user = UserService.get_user_by_id(db, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@router.get("/users/name/{user_name}", response_model=UserResponse)
def get_user(user_name: str, db: Session = Depends(get_db)):
    user = UserService.get_user_by_name(db, user_name)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user


@router.put("/users/{user_id}", response_model=UserResponse)
def update_user(user_id: str, user_data: UserUpdate, db: Session = Depends(get_db)):
    user = UserService.update_user(db, user_id, user_data)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user


@router.delete("/users/{user_id}", response_model=UserResponse)
def delete_user(user_id: str, db: Session = Depends(get_db)):
    user = UserService.delete_user(db, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user
