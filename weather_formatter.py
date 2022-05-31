
from weather_api_service import Weather


def format_weather(weather: Weather) -> str:
    """Format weather data to string"""
    return f"{weather.city} {weather.temperature} {weather.weather_type}"