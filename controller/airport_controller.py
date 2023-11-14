from model.aircraft import Aircraft
from model.flight import Flight
from model.airline import Airline
from model.passenger import Passenger
from model.crew import Crew
from model.control_tower import ControlTower
from view.errorMessage import errorMessage
import datetime

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
        self._flights : dict[str, Flight]= {}

    ###### Aircrafts ######
    
    def get_aircrafts( self ):
        res = []
        for air in self._aircrafts.values():
            res.append( ( air.getN_number(), air.getBrand(), air.getModel(), air.getYearProduction(), air.getAbilityPass(), air.getSpeedMax(), air.getAutonomy(), air.getAsociatedFlights(), air.isInFlight(), air.inManteinance(),  air.canAssignFlight(), air.getOriginFlights() ) )
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

    def whatIs(self, aircraft) -> str:
        return str(type(self._aircrafts[aircraft])).split(".")[1]
    
    def get_espefic_aircraft(self, aricraft : str) -> list:
        tmp = vars(self._aircrafts[aricraft])
        ans  = {clave[1:]: valor for clave, valor in tmp.items()}
        del ans["originFlights"] 
        if "owner" in ans:
            tmp = vars(ans["owner"])
            ans["owner"] = {clave[1:]: valor for clave, valor in tmp.items()}
        return ans

    ##### Passager ######

    def create_passager( self, cedula: str, name: str, surname: str, birthDate: str, genre: str, address: str, phoneNumber: str, email: str, nationality : str, medicalInfo : str, luggageAmount : int) -> None:
        if ( cedula in self._passengers ):
            errorMessage( "Error: la cedula %s ya esta utilizada por otro pasajero." % ( cedula ) )
            return;
        self._passengers[cedula] = Passenger(cedula, name, surname, birthDate, genre, address, phoneNumber, email, nationality, medicalInfo, luggageAmount )

    def get_passenger_generic(self, idFlight : str = None) -> list[tuple[str]]:
        ans = []
        if idFlight is None:
            passengers = self._passengers.values()
        else:
            if not idFlight in self._flights:
                errorMessage( "Error: no existe un vuelo con ese codigo de identificacion.")
                return
            passengers = self._flights[idFlight].getPassengers().values()

        for pas in passengers:
            ans.append( (pas.getCedula(), pas.getName(), pas.getSurname(), pas.getBirthDate(), pas.getGenre(), pas.getAddress(), pas.getPhoneNumber(), pas.getEmail(), pas.getNationality(), pas.getMedicalInfo(), pas.getLuggageAmount()) )
        return ans
    
    def assign_passenger_to_flight(self, cedula : str, idFlight : str) -> None:
        if not cedula in self._passengers:
            errorMessage( "Error: la cedula %s no se encuentra registrada." % ( cedula ) )
            return
        self._flights[idFlight].bookSeat(self._passengers[cedula])

    def del_passenger(self, cedula : str) -> None:
        if not cedula in self._passengers:
            errorMessage( "Error: la cedula %s no se encuentra registrada." % ( cedula ) )
            return
        del self._passengers[cedula]


    ###### Crew ######

    def get_crews( self ):
        res = []
        for crew in self._crews.values():
            res.append( ( crew.getCedula(), crew.getName(), crew.getSurname(), crew.getBirthDate(), crew.getGenre(), crew.getAddress(), crew.getPhoneNumber(), crew.getEmail(), crew.getJobPosition(), crew.getDailyWorkingHours(), crew.getYearsExperience() ) )
        return res;

    # Crea un nuevo tripulante
    def create_crew(self, cedula: str, name: str, surname: str, birthDate: datetime.date, genre: str, address: str, phoneNumber: str, email: str, jobPosition: str, dailyWorkingHours: int, yearsExperience: int) -> None:
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

    def there_pilot(self, crews : list[str]) -> bool:
        ans = False
        for crew in crews:
            if self._crews[crew].getJobPosition() == "piloto":
                ans = True
                break
        return ans

    ###### Airline ######

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

    ###### Airport ######
    
    def get_airports( self ) : 
        res = [];
        for airp in self._airports.values():
            res.append( (airp.getCity(),airp.getAmountFlights(), airp.availableGates()) );
        return res;

    def create_airport( self, city : str ) :
        if ( city in self._airports ):
            errorMessage( "Error: el nombre del aeropuerto %s ya esta tomado" % ( city ) )
            return;
        self._airports[city] = ControlTower(city);

    def delete_airport( self, city : str ) :
        if ( self._airports[city].getAmountFlights() > 0 ):
            errorMessage( "Error: el aeropuerto tiene varios vuelos asignados" );
            return;
        del self._airports[city]

    ###### Boarding Gate ######
    
    def get_boardingGates( self, city : str ) :
        tmp = self._airports[city].getBoardingGates();
        res = []
        for gate in tmp:
            res.append( (gate.getIdentification(), gate.getLocation(), gate.getInGate(), gate.getHistory() ) );
        return res;

    def create_boardingGate( self, city : str, ide : str, loc : str ):
        tmp = self._airports[city].getBoardingGates();
        for gate in tmp:
            if ( gate.getIdentification() == ide ):
                errorMessage( "Error: el aeropuerto %s tiene ya la puerta de embarque de nombre %s" % ( city, ide ) )
                return;
        self._airports[city].addGate( ide, loc );

    def delete_boardingGate( self, city : str, ide : str ):
        self._airports[city].deleteGate( ide );
    
    ###### flight #######

    def get_flights_generic ( self, elem : str, key : str, fun = lambda x:True ):
        res = []
        if ( elem == "airline" ):
            flights = self._airlines[key].getSimpleFlights();
        elif ( elem == "airport" ):
            flights = self._airports[key].getFlights();
        elif ( elem == "client"):
            flights = self._flights.values()
        else:
            raise Exception( "Error: La funcion <get_flights_generic> de la clase <AirportController> no reconoce 'elem' = %s" %(elem) );
        for f in flights:
            if fun( f ) :
                aircraft = f.getAircraft();
                res.append( ( f.getFlightCode(), f.getDate(), f.getOrigin(), f.getDestiny(), aircraft.getN_number(),  f.getCrewMates(), str(f.getBookedSeats()) + "/" + str(f.getTotalSeats()) ,f.isInAir() ) )
        return res
    
    def create_flight( self, airline : str, aircraft : str, flightCode : str, date : datetime.date, origin : str, destiny : str, crews : list[str] ):
        if flightCode in self._flights:
            errorMessage( "Error: el codigo %s ya esta en uso." % ( flightCode ) )
            return;
        f = Flight( self._aircrafts[aircraft], crews, flightCode, date, origin, destiny )
        self._flights[flightCode] = f
        self._airlines[airline].addFlight( f )
        #no se que mas queras hacerle aqui

    def cancel_flight( self, airline : str, flightId : str ) -> None :
        self._airlines[airline].deleteFlight( flightId );

    def start_flight( self, airline : str, flightId : str ) -> None :
        flight = self._airlines[airline].getFlight( flightId );
        
        if ( not self._airlines[airline].canActivateFlight( flightId ) ):
            raise Exception( "Error: es imposible activar el vuelo porque esta en mantenimiento o en otro vuelo" )

        if ( flight.getOrigin() in self._airports ):
            if ( self._airports[flight.getOrigin()].availableGates() == 0 ):
                errorMessage( "Error: no hay suficientes puertas de abordaje en el aeropuerto %s" %(flight.getOrigin()) )
            else:
                self._airlines[airline].activateFlight( flightId )
                self._airports[flight.getOrigin()].addFlight( flight )

        elif ( flight.getDestiny() in self._airports ):
            self._airports[flight.getDestiny()].addFlight( flight )


    ## Control Tower ##

    def takeOff_flight( self, airport : str, flight : str ) :
        self._airports[airport].flightTakeOff( flight );

    def land_flight( self, airport : str, flight : str ) :
        if ( self._airports[airport].availableGates() == 0 ):
            errorMessage( "Error: no hay suficientes puertas de abordaje en el aeropuerto %s" %(airport) )
            return;
        self._airports[airport].flightLand( flight );

    def end_flight( self, airport : str, flight : str ) :
        self._airports[airport].endFlight( flight );

    def continue_flight( self, airport : str, flightId : str ) :
        flight = self._airports[airport].continueFlight( flightId );
        if ( flight.getDestiny() in self._airports ):
            self._airports[flight.getDestiny()].addFlight( flight )

    def isInAir(self, idFlight : str) -> bool:
        if not idFlight in self._flights:
            errorMessage("Eror: no existe un vuelo con este codigo %s" %(idFlight))
            return
        ans = self._flights[idFlight].isInAir()
        return ans
    
    def notifyFlights(self, idFlight : str, airport : str ):
        m = self._flights[idFlight].getFlightInformation()
        self._airports[airport].notifyFlights(m)
        tmp = m.getInfo()
        ans = " | ".join([tmp[0], str(tmp[1]), str(tmp[2]), str(tmp[3]), str(tmp[4]), str(tmp[5])])
        return ans

    def get_messages_flight(self, flight : str) -> list:
        return self._flights[flight].getHistoryMessages()


