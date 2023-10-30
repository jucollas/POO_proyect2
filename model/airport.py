#from model.aircraft_factory import AircraftFactory
from model.crew import Crew


class Airport:
    
    def __init__(self) -> None:
        self._crews : dict[str, Crew] = {}
        self._passegers : dict = {}
        self._aircrafts : dict = {}
        #self._airlines : dict = {}
        #self._boarding : dict = {}

    def create_crew(self, cedula : str, name : str, surname : str, birthDate : str, genre : str, address : str, phoneNumber : str, email : str, jobPosition : str, dailyWorkingHours : int, yearsExperience : int) -> None:
        self._crews[cedula] = Crew(cedula, name, surname, birthDate, genre, address, phoneNumber, email, jobPosition, dailyWorkingHours, yearsExperience)

    def modify_crew(self, cedula : str, name : str = None, surname : str = None, birthDate : str = None, genre : str = None, address : str = None, phoneNumber : str = None, email : str = None, jobPosition : str = None, dailyWorkingHours : int = None, yearsExperience : int = None) -> None:

        if not cedula in self._crews:
            raise Exception( "Error: There is no crew member with that identification number.")
        else:
            if name != None:
                self._crews[cedula].
            if
        print("falta")

    def search_crew(self) -> None:
        print("falta")

    def create_passager(self) -> None:
        print("falta")

    def modify_passager(self) -> None:
        print("falta")

    def search_passager(self) -> None:
        print("falta")

    def create_aircraft(selfr) -> None:
        print("falta")

    def modify_aircraft(selfr) -> None:
        print("falta")

    def search_aircraft(self) -> None:
        print("falta")


        

