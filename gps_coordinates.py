
from dataclasses import dataclass
from typing import Literal
import os

from exceptions import CantGetCoordinates
import config


@dataclass(slots=True, frozen=True)
class Coordinates:
    latitude: float
    longitude: float


def get_gps_coordinates() -> Coordinates:
    """Return current gps coordinates"""

    coordinates = _get_coordinates_from_file()
    return _round_coordinates(coordinates)


def _get_coordinates_from_file() -> Coordinates:
    filename = "coordinates.txt"
    lines = _get_strings_from_file(filename)

    return Coordinates(
        latitude=_parse_coordinate(lines, "latitude"),
        longitude=_parse_coordinate(lines, "longitude")
    )


def _get_strings_from_file(filename: str) -> list[str]:
    if not (os.path.exists(filename)):
        raise CantGetCoordinates("file not exists")

    with open(filename, encoding="utf-8") as f:
        try:
            lines = f.readlines()
        except UnicodeDecodeError:
            raise CantGetCoordinates("file decode error")
    
    if len(lines) == 0:
        raise CantGetCoordinates("file is empty")

    return lines


def _parse_coordinate(
    lines: list[str],
    coord_type: Literal["latitude", "longitude"]) -> float:

    coordinate = None
    for line in lines:
        line = line.strip().lower()
        if line.startswith(f"{coord_type}:"):
            try:
                coordinate = float(line.split()[1])
            except ValueError:
                raise CantGetCoordinates("parsing to float error")
    
    if coordinate is None:
        raise CantGetCoordinates("coordinate not found")
    else:
        return coordinate


def _round_coordinates(coordinates: Coordinates) -> Coordinates:
    if not config.USE_ROUNDED_COORDINATES:
        return coordinates

    return Coordinates(*map(
        lambda c: round(c, 1),
        [coordinates.latitude, coordinates.longitude]
    ))
