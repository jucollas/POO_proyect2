from model.person import Person
import datetime

class Airport_Controller:

    def __init__(self) -> None:
        self._passengers : list = []
        
    def create_person(self, cedula : str, name : str, surname : str, birthDate : datetime.date, genre : str, address : str, phoneNumber : str, email : str) -> None:
        p = Person(cedula, name, surname, birthDate, genre, address, phoneNumber, email)
        self._passengers.append(p)

        
