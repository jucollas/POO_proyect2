from person import Person

class Passenger(Person):
    def __init__(self, cedula : str, name : str, surname : str, birthDate : str, genre : str, address : str, phoneNumber : str, email : str, nationality : str, medicalInfo : str, luggageAmount : int):
        super().__init__(cedula, name, surname, birthDate, genre, address, phoneNumber, email)
        self._nationality = nationality
        self._medicalInfo = medicalInfo
        self.luggageAmount = luggageAmount

    def getNationality(self):
        return self._nationality

    def getMedicalInfo(self):
        return self._medicalInfo

    def setMedicalInfo(self, medicalInfo):
        self._medicalInfo = medicalInfo

    def info(self):
        print(super().info())
        print(f".Medical information: {self.medicalInfo}.")
