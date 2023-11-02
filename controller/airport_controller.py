from model.aircraft import Aircraft
from model.aircraft_factory import AircraftFactory
from model.flight import Flight
from model.airline import Airline
from model.passenger import Passenger
from model.crew import Crew

class AirportController:
    # patron singleton
    _instance = None

    def __new__(cls) -> 'AirportController':
        if cls._instance is None:
            cls._instance = super(AirportController, cls).__new__(cls)
            cls._instance._init_controller()
        return cls._instance

    def _init_controller(self) -> None:
        self._airlines : dict[str, Airline] = {}
        self._aircrafts : dict[str, Aircraft] = {}
        self._crews : dict[str, Crew] = {}
        self._passegers : dict[str, Passenger] = {}
        self._flights :  dict[str, Flight] = {}

    # Crea un nuevo tripulante
    def create_crew(self, cedula: str, name: str, surname: str, birthDate: str, genre: str, address: str, phoneNumber: str, email: str, jobPosition: str, dailyWorkingHours: int, yearsExperience: int) -> None:
        self._crews[cedula] = Crew(cedula, name, surname, birthDate, genre, address, phoneNumber, email, jobPosition)

    # Elimina un tripulante de todo el sistema
    def delete_crew(self, cedula: str) -> None:
        self.delete_crew_memeder_to_flight(cedula)
        del self._crews[cedula]

    # Elimina un triptante del vuelo que tiene asigando
    def delete_crew_memeder_to_flight(self, cedula : str) -> None:
        for flight in self._flights.values():
            if flight.this_crew_member(cedula):
                flight.delete_crew_member(cedula)
                break
    
    # Asigna un tripulante a un vuelo
    def assign_crew_member_to_flight(self, cedulaCrew : str, flightCode : str) -> None:
        self._flights[flightCode].bookSeat(self._crews[cedulaCrew])
