import datetime

class Message:
    
    def __init__(self, latitude : float, longitude : float, height : float, flightCode : str, date : datetime.date) -> None:
        self._date : datetime = date
        self._latitude = latitude
        self._longitude = longitude
        self._height = height
        self._flightCode = flightCode

    def getFlightCode(self) -> str:
        return self._flightCode

    def getInfo(self) -> tuple:
        ans = (self._flightCode, self._date, self._height, self._latitude, self._longitude)
        return ans

    def __str__(self) -> None:
        return f"Latitude: {self._latitude}, Longitude: {self._longitude}, Height: {self._height}, Flight Code: {self._flightCode}"

if __name__ == "__main__":
    x1 = Message( 1.0,2.0,4.5, "hola" );
    print(x1)