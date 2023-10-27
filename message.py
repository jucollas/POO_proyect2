class Message:
    def __init__(self, latitude : float = None, longitude : float = None, height : float = None, flightCode : float = None):
        self._latitude = latitude
        self._longitude = longitude
        self._height = height
        self._flightCode = flightCode

    def __str__(self):
        return f"Latitude: {self.latitude}, Longitude: {self.longitude}, Height: {self.height}, Flight Code: {self.flightCode}"
