
from typing import Protocol, TypedDict
from datetime import datetime
from pathlib import Path
import json

from weather_api_service import Weather
from weather_formatter import format_weather
from exceptions import HistoryError


class WeatherStorage(Protocol):
    """Interface for any storage saving weather"""

    def save(self, weather: Weather) -> None:
        raise NotImplementedError


class PlainFileWeatherStorage:
    """Store weather in plain text file"""

    def __init__(self, file: Path):
        self._file = file

    def save(self, weather: Weather) -> None:
        now = datetime.now()
        formatted_weather = format_weather(weather)
        try:
            with open(self._file, "a") as f:
                f.write(f"{now}\n{formatted_weather}\n")
        except:
            raise HistoryError("saving history error")


class HistoryRecord(TypedDict):
    date: str
    weather: str


class JSONFileWeatherStorage:
    """Store weather in JSON file"""

    def __init__(self, jsonfile: Path):
        self._jsonfile = jsonfile
        self._init_storage()

    def _init_storage(self) -> None:
        if not self._jsonfile.exists():
            try:
                self._jsonfile.write_text("[]")
            except:
                raise HistoryError("init history storage error")

    def save(self, weather: Weather) -> None:
        history = self._read_history()
        history.append(HistoryRecord(
            date=str(datetime.now()),
            weather=format_weather(weather)
        ))
        self._write(history)

    def _read_history(self) -> list[HistoryRecord]:
        try:
            with open(self._jsonfile, "r") as f:
                return json.load(f)
        except:
            raise HistoryError("reading history error")

    def _write(self, history: list[HistoryRecord]) -> None:
        try:
            with open(self._jsonfile, "w") as f:
                json.dump(history, f, ensure_ascii=False, indent=4)
        except:
            raise HistoryError("saving history error")


def save_weather(weather: Weather, storage: WeatherStorage) -> None:
    """Saves weather in the storage"""
    
    storage.save(weather)