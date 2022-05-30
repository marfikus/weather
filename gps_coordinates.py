
from typing import NamedTuple


class Coordinates(NamedTuple):
    latitude: float
    longitude: float


def get_gps_coordinates() -> Coordinates:
    """Return current gps coordinates"""
    return Coordinates(10, 20)
