#from model.aircraft_factory import AircraftFactory
from model.crew import Crew


class Airport:
    
    def __init__(self) -> None:
        self._crews : dict = {}
        self._passegers : dict = {}
        #self._airlines : dict = {}
        #self._aircrafts : dict = {}
        #self._boarding : dict = {}

    def create_crew(self, cedula : str, name : str, surname : str, birthDate : str, genre : str, address : str, phoneNumber : str, email : str, jobPosition : str, dailyWorkingHours : int, yearsExperience : int) -> None:
        self._crews[cedula] = Crew(cedula, name, surname, birthDate, genre, address, phoneNumber, email, jobPosition, dailyWorkingHours, yearsExperience)

        

