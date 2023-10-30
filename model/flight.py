
from model.message import Message
from model.person import Person
from model.passenger import Passenger
from model.crew import Crew
from model.aircraft import Aircraft
from model.abstract_flight import AbsFlight
from model.control_tower import ControlTower


import random
import time
import datetime

class Flight(AbsFlight):
    def __init__(self, aircraft : Aircraft, crewMates : list[Crew], flightCode : str, date : datetime.date, origin : str, destiny : str ):
        self._aircraft = aircraft
        self._control = None
        self._crewMates = crewMates
        self._flightCode = flightCode
        self._date = date
        self._origin = origin
        self._destiny = destiny
        self._activeFlight = False
        self._alreadyFlew = False
        self._gateId = None
        self._passengers = []
        aircraft.assignFlight()

    # get
    
    def getGateId(self):
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

    def getPassengers(self) -> list[Passenger] :
        return self._passengers.copy() # para evitar cambios raros en self._passengers

    def getCrewMates(self) -> list[Crew] :
        return self._crewMates.copy() # para evitar cambios raros en self._crewMates

    # set

    def setControlTower( self, controlTower ) -> None :
        self._control = controlTower

    def setBoardingGate( self, boardingGate ) -> None :
        self._gateId = boardingGate

    # functiones

    def sendFlightInformation(self) -> None :
        if not self.isActive() or self._control is None :
            return

        random.seed(time.time())
        latitude = round(random.uniform(-90, 90), 2)
        height = random.randint(-9000, 9000)
        longitude = round(random.uniform(-180, 180), 2)
        message = Message(longitude, latitude, height, self.flightCode)
        self._control.notifyFlights(message)

    def receiveMessage( self, message : Message ) -> None :
        if message.flightCode != self.flightCode:
            print(f"{self.flightCode} received the message: %s" % ( str( message ) ) )

    def land (self ) -> None :
        if not self.isActive():
            print("The flight is not active")
        elif not self.isInAir():
            print("Was already on land")
        elif self._control is None:
            print( "No control tower connected" )
        else:
            self._gateId = self._control.bookBoardingGate(self)
            if not self._gateId:
                print("Unable to land")
            else:
                print(f"Landed. The assigned boarding gate is: {self._gateId}")

    def takeOff(self):
        if not self.isActive():
            print("The flight is not active")
        elif self.isInAir():
            print("The flight is already in the air")
        else:
            self._control.freeBoardingGate(self._gateId)
            self._gateId = None
            print("The take-off was successful")

    def activateFlight( self ) -> bool :
        res = not self.isActive() and not self._alreadyFlew
        res = res and not self._aircraft.isInFlight() and not self._aircraft.inManteinance()
        if res:
            self._activeFlight = True
            self._aircraft.activateFlight()
        return res

    def endFlight( self ):
        res = self.isActive()
        if res:
            if ( self._gateId is not None ):
                self._control.freeBoardingGate( self._gateId )
            self._control.deleteFlight(self)
            self._activeFlight = False
            self._alreadyFlew = True
        return res

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

    def bookSeat(self, passenger):
        res = self.hasAvailableSeats()
        if res:
            self._passengers.append(passenger)
        else:
            raise Exception("Error: there are not enough seats.")
        return res

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
    print(f1)
    print(f2)
    print(f3)
    ct = ControlTower( "cali" );
    ct.addGate("00", "a")
    ct.addGate("01", "b")
    print( ct )
    f1.activateFlight();
    ct.addFlight( f1 )
    f2.activateFlight()
    ct.addFlight( f2 )
    print( f1)
    print( f2 )
