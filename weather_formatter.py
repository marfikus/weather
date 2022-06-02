
from weather_api_service import Weather


def format_weather(weather: Weather) -> str:
    """Format weather data in string"""
    return (f"---\n{weather.city}, температура {weather.temperature}°C, "
            f"{weather.weather_type}\n"
            f"Восход: {weather.sunrise.strftime('%H:%M')}\n"
            f"Закат: {weather.sunset.strftime('%H:%M')}\n---\n")


if __name__ == "__main__":
    from datetime import datetime
    from weather_api_service import WeatherType

    print(format_weather(Weather(
        temperature=20,
        weather_type=WeatherType.CLEAR,
        sunrise=datetime.fromisoformat("2022-05-30 04:30:00"),
        sunset=datetime.fromisoformat("2022-05-30 22:30:00"),
        city="London"
    )))