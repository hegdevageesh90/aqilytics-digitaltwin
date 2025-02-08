import requests

from app.core.logger import get_logger
from app.core.config import settings

logger = get_logger()


def fetch_aqi_data(latitude: float, longitude: float):
    try:
        logger.info(f"Fetching AQI data for coordinates: ({latitude}, {longitude})")
        url = f"https://api.waqi.info/feed/geo:{latitude};{longitude}/?token={settings.AQI_API_KEY}"
        response = requests.get(url)
        data = response.json()
        if data.get('status') == 'ok':
            logger.info(f"Successfully fetched AQI: {data['data']['aqi']}")
            return data['data']['aqi']
        else:
            logger.error(f"Failed to fetch AQI data. Error: {data.get('data')}")
            raise ValueError("Failed to fetch AQI data.")
    except Exception as e:
        logger.error(f"Error fetching AQI data: {str(e)}")
        raise e
