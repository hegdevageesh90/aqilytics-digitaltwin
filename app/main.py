from fastapi import FastAPI
from app.api import user, aqi, event, notification
from app.db.database import engine
from app.db.models import Base
from app.core.logger import get_logger
from app.core.config import settings

logger = get_logger()

Base.metadata.create_all(bind=engine)

app = FastAPI(title=settings.APP_NAME, prefix=settings.API_PREFIX)

logger.info(f"{settings.APP_NAME} is starting up with API prefix: {settings.API_PREFIX}")

app.include_router(user.router)
app.include_router(aqi.router)
app.include_router(event.router)
app.include_router(notification.router)
