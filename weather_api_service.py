# http://api.openweathermap.org/data/2.5/weather?q=London,uk&APPID=b387cfbee33eb301996acc50708ea0ff

from dataclasses import dataclass
from datetime import datetime
from enum import Enum

from gps_coordinates import Coordinates


Celsius = int

class WeatherType(str, Enum):
    THUNDERSTORM = "Гроза"
    DRIZZLE = "Изморозь"
    RAIN = "Дождь"
    SNOW = "Снег"
    CLEAR = "Ясно"
    FOGS = "Туман"
    CLOUDS = "Облачно"


@dataclass(slots=True, frozen=True)
class Weather:
    temperature: Celsius
    weather_type: WeatherType
    sunrise: datetime
    sunset: datetime
    city: str


def get_weather(coordinates: Coordinates) -> Weather:
    """Request weather in API service"""
    return Weather(
        temperature=20,
        weather_type=WeatherType.CLEAR,
        sunrise=datetime.fromisoformat("2022-05-31 04:00:00"),
        sunset=datetime.fromisoformat("2022-05-31 22:00:00"),
        city="Shadrinsk"
    )

