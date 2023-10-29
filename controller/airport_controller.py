from model.person import Person

class Airport_Controller:

    def __init__(self) -> None:
        self._passengers : list = []
        
    def create_person(self, cedula : str, name : str, surname : str, birthDate : str, genre : str, address : str, phoneNumber : str, email : str) -> None:
        p = Person(cedula, name, surname, birthDate, genre, address, phoneNumber, email)
        self._passengers.append(p)

        
