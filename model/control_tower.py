
from abstract_flight import AbsFlight
from message import Message
from gate_control import GateControl


class ControlTower:
    def __init__( self, city : str ):
        self._flights : set[AbsFlight] = set()
        self._gateControl = GateControl()
        self._city = city;

    def getCity( self ) -> str :
        return self._city

    def getFlights( self ) -> list[AbsFlight] :
        res = []
        for f in self._flights:
            res.append( f )
        return res

    def addFlight(self, f: AbsFlight) -> None:
        self._flights.add( f )
        f.setControlTower( self )

    def deleteFlight(self, f: AbsFlight) -> None:
        if f in self._flights:
            self._flights.discard( f )
            f.setControlTower( None )

    def notifyFlights(self, m: Message) -> None:
        for f in self._flights:
            f.receiveMessage(m)

    def bookBoardingGate(self, f: AbsFlight) -> str:
        return self._gateControl.bookBoardingGate(f)

    def freeBoardingGate(self, gate_id: str) -> None:
        self._gateControl.freeBoardingGate( gate_id )

    def addGate(self, gateId: str, location: str) -> None:
        self._gateControl.addGate( gateId, location)

    def getFlights( self ) -> set[AbsFlight] :
        return self._flights.copy()

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


