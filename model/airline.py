
import model.connections as connections
from model.flight import Flight
from model.passenger import Passenger
import datetime

class Airline:
    def __init__(self, name : str ):
        self._name = name
        self._scheduled_flights: dict[str, Flight] = {}

    def getName( self ) -> str :
        return self._name

    def getAmountFlights( self ) -> int :
        return len( self._scheduled_flights );

    def getFlights( self ) :
        res = []
        for f in self._scheduled_flights.values():
            res.append( f );
        return res;

    def scheduleFlight(self, flight_id: str, passenger: Passenger) -> bool:
        res = False
        if flight_id not in self.scheduled_flights:
            print( "Error: the flight %s doesnt exist" % (flight_id) )
        elif self._scheduled_flights[flight_id].has_available_seats():
            res = self._scheduled_flights[flight_id].book_seat(passenger)
        else:
            raise Exception("Error: not enough space in the aircraft.")
        return res

    def filterFlight(self, date : datetime.date = None, origin : str = None, destiny: str = None) -> list[Flight]:
        res = []
        for flight in self._scheduled_flights.values():
            if (date is None or date == flight.get_date()) and (origin is None or origin == flight.get_origin()) and (destiny is None or destiny == flight.get_destiny()):
                #booked_seats = flight.get_booked_seats()
                #ability_pass = flight.get_aircraft().get_ability_pass()
                #print(f"[{len(res)}] {flight.get_flight_code()} | date: {flight.get_date()}, origin: {flight.get_origin()}, destiny: {flight.get_destiny()}. With [{booked_seats}/{ability_pass}] available seats.")
                res.append(flight)
        return res

    def addFlight(self, flight: Flight) -> None:
        self._scheduled_flights[flight.getFlightCode()] = flight

    def deleteFlight( self, flightId : str ) -> None :
        del self._scheduled_flights[flightId];

    def activateFlight( self, flightId : str ) -> None :
        if flightId in self._scheduled_flights:
            flight = self._scheduled_flights[flightId]
            flight.activateFlight();
            if ( flight.getOrigin() in connections.cities ):
                connections.cities[flight.getOrigin()].addFlight( flight )
                flight.setBoardingGate( connections.cities[flight.getOrigin()].bookBoardingGate( flight ) )
            del self._scheduled_flights[flightId]


    def unscheduleFlight(self, flight_id: str) -> None:
        if flight_id in self._scheduled_flights:
            del self._scheduled_flights[flight_id]

    def __str__(self) -> str:
        tmp = [f"There are {len(self._scheduled_flights)} scheduled flights."]
        for flight in self._scheduled_flights.values():
            tmp.append( flight.__str__() )
        return "\n".join( tmp );

if __name__ == "__main__":
    from control_tower import ControlTower
    from flight import Flight
    from aircraft import Aircraft
    ai = Airline( "avianca" );
    connections.airlines[ai.getName()] = ai
    ct = ControlTower( "cali" )
    ct.addGate( "00", "a" )
    connections.cities[ct.getCity()] = ct
    av = Aircraft( "tango-00", "boeing", "airbus", "anteayer", 100, 200, 300  );
    f1 = Flight( av, [], "cactus-88", datetime.date( 2020, 12, 7 ), "cali", "barranquilla" )
    ai.addFlight( f1 )
    print( ai )
    ai.activateFlight( f1.getFlightCode() );
    print ( ai )
    print( ct )
    f1.takeOff();
    print( ct )
    f1.disconnectFlight();
    print(f1)
    ct.addFlight(f1)
    f1.land()
    print(ct)
    f1.endFlight()
    print(ct)
    print(airlines)


