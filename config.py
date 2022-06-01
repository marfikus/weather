
from api_key import OPENWEATHER_APP_ID

USE_ROUNDED_COORDINATES = True

# http://api.openweathermap.org/data/2.5/weather?q=London,uk&APPID=b387cfbee33eb301996acc50708ea0ff&lang=ru&unuts=metric
# http://api.openweathermap.org/data/2.5/weather?lat=56.1&lon=63.6&APPID=b387cfbee33eb301996acc50708ea0ff&lang=ru&units=metric

OPENWEATHER_API_URL = (
    "http://api.openweathermap.org/data/2.5/weather?lat={latitude}&lon={longitude}&APPID=" + OPENWEATHER_APP_ID + "&lang=ru&units=metric"
)
