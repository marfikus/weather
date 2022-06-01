
class CantGetCoordinates(Exception):
    """Program can't current gps coordinates"""

    def __init__(self, value):
        self.msg = value

    def __str__(self):
        return self.msg

class ApiServiceError(Exception):
    """Api service error"""