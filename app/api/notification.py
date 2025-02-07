from fastapi import APIRouter, BackgroundTasks
from app.services import notification_service

router = APIRouter()


@router.post("/notifications")
def send_aqi_notification(user_id: str, message: str, background_tasks: BackgroundTasks):
    notification_service.send_notification(background_tasks, user_id, message)
    return {"status": "Notification Sent"}
