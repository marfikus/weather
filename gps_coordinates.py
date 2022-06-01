
from dataclasses import dataclass
from exceptions import CantGetCoordinates
import os
import config


@dataclass(slots=True, frozen=True)
class Coordinates:
    latitude: float
    longitude: float


def get_gps_coordinates() -> Coordinates:
    """Return current gps coordinates"""

    filename = "coordinates.txt"

    if not (os.path.exists(filename)):
        raise CantGetCoordinates("file not exists")

    with open(filename, encoding="utf-8") as f:
        lines = f.readlines()
    
    if len(lines) == 0:
        raise CantGetCoordinates("file is empty")

    latitude = longitude = None

    for line in lines:
        line = line.strip().lower()
        if line.startswith("latitude"):
            latitude = float(line.split()[1])
        if line.startswith("longitude"):
            longitude = float(line.split()[1])

    if config.USE_ROUNDED_COORDINATES:
        latitude, longitude = map(lambda c: round(c, 1), [latitude, longitude])

    return Coordinates(latitude=latitude, longitude=longitude)

# print(get_gps_coordinates())