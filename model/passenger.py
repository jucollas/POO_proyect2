from model.person import Person

class Passenger(Person):
    def __init__(self, cedula : str, name : str, surname : str, birthDate : str, genre : str, address : str, phoneNumber : str, email : str, nationality : str, medicalInfo : str, luggageAmount : int):
        super().__init__(cedula, name, surname, birthDate, genre, address, phoneNumber, email)
        self._nationality = nationality
        self._medicalInfo = medicalInfo
        self._luggageAmount = luggageAmount

    def getNationality(self) -> str:
        return self._nationality

    def getMedicalInfo(self) -> str:
        return self._medicalInfo
    
    def getLuggageAmount(self) -> int:
        return self._luggageAmount

    def setMedicalInfo(self, medicalInfo):
        self._medicalInfo = medicalInfo

    def __str__(self) -> str :
        tmp = [super().__str__()]
        tmp.append( f"Medical information: {self._medicalInfo}" );
        return ". ".join( tmp );

if __name__ == "__main__":
    pas = Passenger( "1110101", "oscar", "vargas", "hoy", "macho", "en tu casa", "0135462013", "hola@gmail.com", "colombiano", "muerto", 5 );
    print( pas )
