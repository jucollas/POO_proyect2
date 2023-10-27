class Person:
    def __init__(self, cedula : str, name : str, surname : str, birthDate : str, genre : str, address : str, phoneNumber : str, email : str):
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

    def info(self) -> str:
        return f"{self._name} {self._surname}[{self._cedula}]"
