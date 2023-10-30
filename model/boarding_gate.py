from model.abstract_flight import AbsFlight
import datetime


class BoardingGate:
    def __init__(self, identification: str, location: str) -> None:
        self._identification = identification
        self._location = location
        self._inGate = None
        self._history = []

    def getIdentification(self) -> str:
        return self._identification

    def getLocation(self) -> str:
        return self._location

    def getHistory(self) -> list[AbsFlight]:
        return self._history.copy(); # to prevent weird changes in the self.history log

    def getInGate(self) -> str:
        if self._inGate is not None:
            return self._inGate.getFlightCode()
        else:
            return None

    def assignFlight(self, f: AbsFlight) -> bool:
        res = self.isAvailable()
        if res:
            self._inGate = f
        return res

    def dispatchFlight(self) -> None:
        if self._inGate is not None:
            self._history.append(self._inGate)
            self._inGate = None

    def isAvailable(self) -> bool:
        return self._inGate is None

    def __str__ (self) -> str :
        info_str = [f"Gate: {self._identification}, located in {self._location}."]
        if self._inGate is None:
            info_str.append(" It hosts no flight.")
        else:
            info_str.append(f" It hosts flight with code: {self._inGate.getFlightCode()} at {self._inGate.getDate()}.")
        return "".join( info_str );

    def __del__( self ) :
        for h in self._history:
            del ( h )


if __name__ == "__main__":
    bg = BoardingGate( "puerta 00", "al lado de tu casa" );
    from flight import Flight
    from aircraft import Aircraft
    av = Aircraft( "tango-00", "boeing", "airbus", "anteayer", 100, 200, 300  );
    f1 = Flight( av, [], "cactus-88", datetime.date( 2020, 12, 7 ), "cali", "barranquilla" )
    print( bg )
    bg.assign_flight( f1 )
    print( bg );
    bg.dispatch_flight();
    print( bg )

