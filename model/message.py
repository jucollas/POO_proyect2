class Message:
    
    def __init__(self, latitude : float = None, longitude : float = None, height : float = None, flightCode : str = None) -> None:
        self._latitude = latitude
        self._longitude = longitude
        self._height = height
        self._flightCode = flightCode

    def __str__(self) -> None:
        return f"Latitude: {self._latitude}, Longitude: {self._longitude}, Height: {self._height}, Flight Code: {self._flightCode}"

if __name__ == "__main__":
    x1 = Message( 1.0,2.0,4.5, "hola" );
    print(x1)