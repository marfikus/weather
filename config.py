
from api_key import OPENWEATHER_APP_ID

USE_ROUNDED_COORDINATES = True

OPENWEATHER_API_URL = (
    "http://api.openweathermap.org/data/2.5/weather?lat={latitude}&lon={longitude}&APPID=" + OPENWEATHER_APP_ID + "&lang=ru&units=metric"
)
