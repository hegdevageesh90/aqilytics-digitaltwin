from loguru import logger
import sys
import os
from dotenv import load_dotenv

load_dotenv()

LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO").upper()

logger.remove()  # Remove the default logger
logger.add(sys.stdout, level=LOG_LEVEL, format="{time} {level} {message}", enqueue=True)
logger.add("logs/{time:YYYY-MM-DD}.log", level=LOG_LEVEL, format="{time} {level} {message}", rotation="1 day",
           retention="7 days", compression="zip")


def get_logger():
    return logger
