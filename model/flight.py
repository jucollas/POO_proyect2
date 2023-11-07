from model.message import Message
from model.passenger import Passenger
from model.crew import Crew
from model.aircraft import Aircraft

import random
import time
import datetime

class Flight():
    def __init__(self, aircraft : Aircraft, crewMates : list[str], flightCode : str, date : datetime.date, origin : str, destiny : str ):
        self._aircraft = aircraft
        self._flightCode = flightCode
        self._date = date
        self._origin = origin
        self._destiny = destiny
        self._activeFlight = False
        self._alreadyFlew = False
        self._gateId = None
        self._passengers = {}
        self._crewMates = crewMates
        aircraft.assignFlight()

    # get
    
    def getGateId(self) -> str:
        return self._gateId

    def getFlightCode(self) -> str :
        return self._flightCode

    def getDate(self) -> datetime.date :
        return self._date

    def getOrigin(self) -> str :
        return self._origin

    def getDestiny(self) -> str :
        return self._destiny

    def getAircraft(self) -> Aircraft :
        return self._aircraft

    def getPassengers(self) -> dict[str, Passenger] :
        return self._passengers.copy() # para evitar cambios raros en self._passengers

    def getCrewMates(self) -> list[str, Crew] :
        return self._crewMates.copy() # para evitar cambios raros en self._crewMates

    # set

    def setBoardingGate( self, boardingGate ) -> None :
        self._gateId = boardingGate

    # functiones

    def canActivate(self) -> bool:
        return not self.isActive() and not self._alreadyFlew and not self._aircraft.isInFlight() and not self._aircraft.inManteinance();

    def getFlightInformation(self) -> Message :
        if not self.isActive() or self._control is None :
            return None;
        random.seed(time.time())
        latitude = round(random.uniform(-90, 90), 2)
        height = random.randint(-9000, 9000)
        longitude = round(random.uniform(-180, 180), 2)
        message = Message(longitude, latitude, height, self.flightCode)
        return message;

    def receiveMessage( self, message : Message ) -> None :
        if message.flightCode != self.flightCode:
            print(f"{self.flightCode} received the message: %s" % ( str( message ) ) )

    def land (self ) -> None :
        pass

    def takeOff(self) -> None :
        self._gateId = None;

    def activateFlight( self ):
        if self.canActivate():
            self._activeFlight = True
            self._aircraft.activateFlight()
        else:
            raise Exception( "Error: Impossible to activate Flight" );

    def endFlight( self ):
        if self.isActive():
            self._gateId = None
            self._activeFlight = False
            self._alreadyFlew = True
            self._aircraft.deactivateFlight();
        else:
            raise Exception( "Error: Impossible to end Flight" );


    def disconnectFlight( self ):
        if ( self._control is not None ):
            self._control.deleteFlight( self )

    def hasItAlreadyFlew(self):
        return self._alreadyFlew

    def isActive(self):
        return self._activeFlight

    def isInAir(self):
        return ( self._gateId is None ) and self.isActive();

    def hasAvailableSeats(self):
        return len(self._passengers) < self._aircraft.getAbilityPass()

    def bookSeat(self, passenger : Passenger) -> bool:
        res = self.hasAvailableSeats()
        if res:
            self._passengers[passenger.getCedula()] = passenger
        else:
            raise Exception("Error: there are not enough seats.")
        return res
    
    # Valida que un tripulante se encuentre asignado en un vuelo
    def this_crew_member(self, cedula : str) -> bool:
        return self._crewMates in cedula
    
    # Elimina un tripulante del vuelo
    def delete_crew_member(self, cedula : str) -> bool:
        if self.this_crew_member(cedula):
            del self._crewMates[cedula]
        else:
            Exception( "Error: There is no crew member on this flight with this identification number %s." % ( cedula ) )
     
    def getBookedSeats( self ) -> int :
        return len(self._passengers)

    def __str__(self) -> str :
        tmp = ["active" if self.isActive() else "inactive"]
        if self.isActive():
            tmp.append( "and flying." if self.isInAir() else f" and assigned to gate {self._gateId}." )
        tmp.append(f"Flight {self._flightCode} with {len(self._passengers)} passengers. It goes from {self._origin} to {self._destiny}. It is assigned to the aircraft {self._aircraft.getN_number()}")
        return " ".join( tmp )

if __name__ == "__main__":
    av = Aircraft( "tango-00", "boeing", "airbus", "anteayer", 100, 200, 300  );
    f1 = Flight( av, [], "cactus-88", datetime.date( 2020, 12, 7 ), "cali", "barranquilla" )
    f2 = Flight( av, [], "cactus-89", datetime.date( 2020, 12, 7 ), "cali", "barranquilla" )
    f3 = Flight( av, [], "cactus-90", datetime.date( 2020, 12, 7 ), "cali", "barranquilla" )
