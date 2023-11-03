from model.flight import Flight

from model.boarding_gate import BoardingGate

class GateControl:
    def __init__(self):
        self._gates : dict[str, BoardingGate] = {}

    def getGates( self ):
        res = [ gate for gate in self._gates.values() ]
        return res

    def bookBoardingGate(self, flight : Flight ) -> str :
        for gate in self._gates.values():
            if gate.isAvailable():
                if gate.assignFlight(flight):
                    return gate.getIdentification()
        raise Exception("Error: impossible to book a gate")

    def freeBoardingGate(self, gate_id) -> None:
        if gate_id in self._gates:
            gate = self._gates[gate_id]
            if not gate.isAvailable():
                gate.dispatchFlight()
        else:
            raise Exception(f"Error: the gateId '{gate_id}' is not in the gates")

    def addGate(self, gateId : str, location : str ) -> None :
        gate = BoardingGate( gateId, location)
        self._gates[gateId] = gate

    def deleteGate( self, gateId : str ) -> None :
        if ( gateId in self._gates ):
            if ( self._gates[gateId].isAvailable() ):
                del ( self._gates[gateId] );
            else:
                raise Exception( "Error: the gate with id %s has a flight identified as %s." % ( gateId, self._gates[gateId].getInGate() ) );
        else: 
            raise Exception( "Error: the id %s is not part of the boarding gates" % ( gateId ) );

    def availableGates( self ) -> int :
        res = 0
        for gate in self._gates.values():
            if ( gate.isAvailable() ):
                res += 1
        return res

    def __str__(self) -> str :
        tmp = [ f"There are {len(self._gates)} gates:" ]
        for gate in self._gates.values():
            tmp.append( gate.__str__() );
        return "\n".join( tmp );

    def __del__(self):
        for gate in self._gates.values():
            del gate

if __name__ == "__main__":
    gc = GateControl(  );
    print( gc )
    gc.addGate( "01","a" );
    print( gc )
    gc.addGate( "02" , "b" );
    print( gc )
    gc.deleteGate( "01" );
    print( gc );