import logging

from fastapi import BackgroundTasks

logger = logging.getLogger(__name__)


def send_notification(background_tasks: BackgroundTasks, user_id: str, message: str):
    logger.info(f"Sending notification to {user_id}: {message}")
    background_tasks.add_task(_send_push_notification, user_id, message)


def _send_push_notification(user_id: str, message: str):
    logger.info(f"Push notification sent to {user_id}: {message}")
