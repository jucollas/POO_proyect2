
from model.flight import Flight

from model.message import Message
from model.gate_control import GateControl

class ControlTower:
    def __init__( self, city : str ):
        self._flights : dict[ str ,Flight] = {}
        self._gateControl = GateControl()
        self._city = city;

    def getCity( self ) -> str :
        return self._city

    def getFlights( self ) -> list[Flight] :
        res = []
        for f in self._flights.values():
            res.append( f )
        return res

    def getAmountFlights( self ) -> int:
        return len( self._flights );

    def getBoardingGates( self ) :
        return self._gateControl.getGates();

    def addFlight(self, f: Flight) -> None:
        if ( f.getOrigin() == self._city ):
            f.setBoardingGate( self.bookBoardingGate( f ) );
        self._flights[f.getFlightCode()] = f 

    def notifyFlights(self, m: Message) -> None:
        for f in self._flights.values():
            f.receiveMessage(m)

    def availableGates( self ) -> int:
        return self._gateControl.availableGates();

    def bookBoardingGate(self, f: Flight) -> str:
        return self._gateControl.bookBoardingGate( f )

    def freeBoardingGate(self, gate_id: str) -> None:
        self._gateControl.freeBoardingGate( gate_id )

    def addGate(self, gateId: str, location: str) -> None:
        self._gateControl.addGate( gateId, location)
    
    def deleteGate( self, gateId : str ) -> None:
        self._gateControl.deleteGate( gateId );

    def availableGates( self ) -> bool :
        return self._gateControl.availableGates();

    def flightTakeOff( self, flightId : str ) -> None :
        self.freeBoardingGate( self._flights[flightId].getGateId() );
        self._flights[flightId].takeOff();

    def flightLand( self, flightId : str  ) -> None : 
        self._flights[flightId].setBoardingGate( self.bookBoardingGate( self._flights[flightId] ) );
        self._flights[flightId].land()

    def endFlight( self, flightId : str ) -> None : 
        self.freeBoardingGate( self._flights[flightId].getGateId() );
        self._flights[flightId].endFlight()
        del self._flights[flightId]

    def continueFlight( self, flightId : str ) -> Flight :
        flight = self._flights[flightId]
        del self._flights[flightId]
        return flight;

    def __str__( self ) -> str:
        tmp = [ f"There are {len(self._flights)} flights connected to the control tower." ]
        for f in self._flights:
            tmp.append( f.__str__() )
        tmp.append( self._gateControl.__str__() )
        return "\n".join( tmp );

if __name__ == "__main__":
    from flight import Flight
    from aircraft import Aircraft
    import datetime
    ct = ControlTower( "cali" );
    print( ct )
    av = Aircraft( "tango-00", "boeing", "airbus", "anteayer", 100, 200, 300  );
    f1 = Flight( av, [], "cactus-88", datetime.date( 2020, 12, 7 ), "cali", "barranquilla" )
    ct.addFlight( f1 )
    f2 = Flight( av, [], "cactus-89", datetime.date( 2020, 12, 7 ), "cali", "barranquilla" )
    ct.addFlight( f2 )
    f3 = Flight( av, [], "cactus-90", datetime.date( 2020, 12, 7 ), "cali", "barranquilla" )
    ct.addFlight( f3 )
    f3.activateFlight( False )

    print( ct )
    f3.sendFlightInformation()


