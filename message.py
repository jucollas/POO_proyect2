class Message:
    def __init__(self, latitude : float = None, longitude : float = None, height : float = None, flightCode : str = None):
        self.latitude = latitude
        self.longitude = longitude
        self.height = height
        self.flightCode = flightCode

    def __str__(self):
        return f"Latitude: {self.latitude}, Longitude: {self.longitude}, Height: {self.height}, Flight Code: {self.flightCode}"

if __name__ == "__main__":
    x1 = Message( 1.0,2.0,4.5, "hola" );
    print(x1)