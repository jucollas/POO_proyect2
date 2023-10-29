import datetime
class Person:
    def __init__(self, cedula : str, name : str, surname : str, birthDate : datetime.date, genre : str, address : str, phoneNumber : str, email : str):
        self._cedula = cedula
        self._name = name
        self._surname = surname
        self._birthDate = birthDate
        self._genre = genre
        self._address = address
        self._phoneNumber = phoneNumber
        self._email = email

    def getCedula(self) -> str:
        return self._cedula

    def getName(self) -> str:
        return self._name

    def getSurname(self) -> str:
        return self._surname

    def getBirthDate(self) -> str:
        return self._birthDate

    def getGenre(self) -> str:
        return self._genre

    def getAddress(self) -> str:
        return self._address

    def getPhoneNumber(self) -> str:
        return self._phoneNumber

    def getEmail(self) -> str:
        return self._email

    def setAddress(self, address) -> None:
        self._address = address

    def setPhoneNumber(self, phoneNumber) -> None:
        self._phoneNumber = phoneNumber

    def setEmail(self, email) -> None:
        self._email = email

    def __str__ (self) -> str:
        return f"{self._name} {self._surname}[{self._cedula}]"

if __name__ == "__main__":
    p = Person( "1110101", "oscar", "vargas", "hoy", "macho", "en tu casa", "0135462013", "hola@gmail.com" )
    print( p );