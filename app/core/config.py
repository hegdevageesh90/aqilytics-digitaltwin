from pydantic_settings import BaseSettings
import os
from dotenv import load_dotenv

load_dotenv()


class Settings(BaseSettings):
    DATABASE_URL: str = os.getenv("DATABASE_URL", "postgresql://adminuser:password@localhost/digitaltwin")

    AQI_API_KEY: str = os.getenv("AQI_API_KEY", "ecfe2f0ba36e6418a44694114efd47521ec217e3")

    LOG_LEVEL: str = os.getenv("LOG_LEVEL", "INFO")

    APP_NAME: str = os.getenv("APP_NAME", "AirQualityTracker")
    API_PREFIX: str = os.getenv("API_PREFIX", "/api")

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


settings = Settings()
