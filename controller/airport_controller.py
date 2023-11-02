from model.aircraft import Aircraft
from model.aircraft_factory import AircraftFactory
from model.flight import Flight
from model.airline import Airline
from model.passenger import Passenger
from model.crew import Crew
from model.control_tower import ControlTower
from view.errorMessage import errorMessage

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
        self._passengers : dict[str, Passenger] = {}
        self._airports : dict[str, ControlTower] = {}
        self._flights = {}

    def get_aircrafts( self ):
        res = []
        for air in self._aircrafts.values():
            res.append( ( air.getN_number(), air.getBrand(), air.getModel(), air.getYearProduction(), air.getAbilityPass(), air.getSpeedMax(), air.getAutonomy(), air.getAsociatedFlights(), air.isInFlight(), air.inManteinance() ) )
        return res;
    def create_aircraft( self, aircraft : Aircraft ):
        if ( aircraft.getN_number() in self._aircrafts ):
            errorMessage( "Error: el numero de serie %s ya ha sido tomado por otra aeronave." % ( aircraft.getN_number() ) )
            return;
        self._aircrafts[aircraft.getN_number()] = aircraft

    def delete_aircraft( self, nNumber : str ):
        del self._aircrafts[nNumber];

    def change_manteinance( self, nNumber : str, state : bool ):
        self._aircrafts[nNumber].toggleManteinance( state )


    def get_crews( self ):
        res = []
        for crew in self._crews.values():
            res.append( ( crew.getCedula(), crew.getName(), crew.getSurname(), crew.getBirthDate(), crew.getGenre(), crew.getAddress(), crew.getPhoneNumber(), crew.getEmail(), crew.getJobPosition(), crew.getDailyWorkingHours(), crew.getYearsExperience() ) )
        return res;

    # Crea un nuevo tripulante
    def create_crew(self, cedula: str, name: str, surname: str, birthDate: str, genre: str, address: str, phoneNumber: str, email: str, jobPosition: str, dailyWorkingHours: int, yearsExperience: int) -> None:
        if ( cedula in self._crews ):
            errorMessage( "Error: la cedula %s ya esta utilizada por un miembro de la tripulacion." % ( cedula ) )
            return;
        self._crews[cedula] = Crew(cedula, name, surname, birthDate, genre, address, phoneNumber, email, jobPosition, dailyWorkingHours, yearsExperience)

    # Elimina un tripulante de todo el sistema
    def delete_crew(self, cedula: str) -> None:
        self.delete_crew_member_to_flight(cedula)
        del self._crews[cedula]

    # Elimina un triptante del vuelo que tiene asigando
    def delete_crew_member_to_flight(self, cedula : str) -> None:
        for flight in self._flights.values():
            if flight.this_crew_member(cedula):
                flight.delete_crew_member(cedula)
                break
    
    # Asigna un tripulante a un vuelo
    def assign_crew_member_to_flight(self, cedulaCrew : str, flightCode : str) -> None:
        self._flights[flightCode].bookSeat(self._crews[cedulaCrew])

    def get_airlines( self ) :
        res = [];
        for air in self._airlines.values() :
            res.append( (air.getName(), air.getAmountFlights()) );
        return res;

    def create_airline( self, name : str ) -> None :
        if ( name in self._airlines ):
            errorMessage( "Error: el nombre de aerolinea %s ya esta tomado" % ( name ) );
            return;
        self._airlines[name] = Airline( name )

    def delete_airline( self, name : str ) -> None :
        del self._airlines[name]

    def get_airports( self ) : 
        res = [];
        for airp in self._airports.values():
            res.append( (airp.getCity(),airp.getAmountFlights()) );
        return res;

    def create_airport( self, city : str ) :
        if ( city in self._airports ):
            errorMessage( "Error: el nombre del aeropuerto %s ya esta tomado" % ( city ) )
            return;
        self._airports[city] = ControlTower(city);

    def delete_airport( self, city : str ) :
        if ( self._airports.getAmountFlights() > 0 ):
            errorMessage( "Error: el aeropuerto tiene varios vuelos asignados" );
            return;
        del self._airports[city]
    
    def get_boardingGates( self, city : str ) :
        tmp = self._airports[city].get_boardingGates();
        res = []
        for gate in tmp:
            res.append( (gate.getIdentification(), gate.getLocation(), gate.getInGate(), gate.getHistory() ) );
        return res;

    def create_boardingGates( self, city : str, ide : str, loc : str ):
        tmp = self._airports[city].get_boardingGates();
        for gate in tmp:
            if ( gate.getIdentification() == ide ):
                errorMessage( "Error: el aeropuerto %s tiene ya la puerta de embarque de nombre %s" % ( city, ide ) )
                return;
        self._airports[city].addGate( ide, loc );

    def delete_boardingGates( self, city : str, id : str ):
        self._airports[city].deleteGate( ide );