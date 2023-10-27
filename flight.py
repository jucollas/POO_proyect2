from message import Message
from passenger import Passenger
from crew import Crew
from control_tower import ControlTower
from aircraft import Aircraft
import random
import time

class Flight:
    def __init__(self, aircraft : Aircraft, control : ControlTower, crewMates : list[Crew], flightCode : str, date : str, origin : str, destiny : str, latitude : float, longitude : float, height : int):
        self.aircraft = aircraft
        self.control = control
        self.crewMates = crewMates
        self.flightCode = flightCode
        self.date = date
        self.origin = origin
        self.destiny = destiny
        self.latitude = latitude
        self.longitude = longitude
        self.height = height
        self.activeFlight = False
        self.alreadyFlew = False
        self.gateId = ""
        aircraft.assignFlight()
    
    def getGateId(self):
        return self.gateId

    def getFlightCode(self):
        return self.flightCode

    def getDate(self):
        return self.date

    def getOrigin(self):
        return self.origin

    def getDestiny(self):
        return self.destiny

    def getAircraft(self):
        return self.aircraft

    def getPassengers(self):
        return self.passengers

    def getCrewMates(self):
        return self.crewMates

    def sendFlightInformation(self):
        if not self.isActive():
            print("The flight is inactive")
            return
        random.seed(time.time())
        latitude = round(random.uniform(-90, 90), 2)
        height = random.randint(-9000, 9000)
        longitude = round(random.uniform(-180, 180), 2)
        self.setCoordinates(height, latitude, longitude)
        self.infoCord()
        message = Message(longitude, latitude, height, self.flightCode)
        self.control.notifyFlights(message)

    def receiveMessage(self, message):
        if message.flightCode != self.flightCode:
            print(f"{self.flightCode} received the message: latitude({message.latitude}), longitude({message.longitude}), height({message.height}) flightCode({message.flightCode})")

    def land(self):
        if not self.isActive():
            print("The flight is not active")
        elif not self.isInAir():
            print("Was already on land")
        else:
            self.gateId = self.control.bookBoardingGate(self)
            if not self.gateId:
                print("Unable to land")
            else:
                print(f"Landed. The assigned boarding gate is: {self.gateId}")

    def takeOff(self):
        if not self.isActive():
            print("The flight is not active")
        elif not self.isInAir():
            print("The flight is already in the air")
        else:
            self.control.freeBoardingGate(self.gateId)
            self.gateId = ""
            print("The take-off was successful")

    def activateFlight(self, onGround):
        res = not self.isActive() and not self.alreadyFlew
        res = res and not self.aircraft.isInFlight() and not self.aircraft.inManteinance()
        if onGround and res:
            self.gateId = self.control.bookBoardingGate(self)
            res = bool(self.gateId)
        if res:
            self.control.addFlight(self)
            self.activeFlight = True
            self.aircraft.activateFlight()
            print("Flight connected to control tower")
        else:
            print("Impossible to activate flight")
        return res

    def endFlight(self):
        res = self.isActive()
        if res:
            self.control.deleteFlight(self)
            self.activeFlight = False
            self.alreadyFlew = True
            print("Flight disconnected from the control tower")
        else:
            print("Flight unable to disconnect")
        return res

    def hasItAlreadyFlew(self):
        return self.alreadyFlew

    def isActive(self):
        return self.activeFlight

    def isInAir(self):
        return not self.gateId

    def hasAvailableSeats(self):
        return len(self.passengers) < self.aircraft.getAbilityPass()

    def bookSeat(self, passenger):
        res = self.hasAvailableSeats()
        if res:
            self.passengers.append(passenger)
        else:
            print("Error: there are not enough seats.")
        return res

    def getBookedSeats(self):
        return len(self.passengers)

    def setCoordinates(self, height, latitude, longitude):
        self.height = height
        self.latitude = latitude
        self.longitude = longitude

    def info(self):
        status = "active" if self.isActive() else "inactive"
        if self.isActive():
            status += " and flying." if self.isInAir() else f" and assigned to gate {self.gateId}."
        print(f"Flight {self.flightCode} with {len(self.passengers)} passengers. It goes from {self.origin} to {self.destiny}. It is assigned to the aircraft {self.aircraft.getN_number()}. It's {status}")

    def infoCord(self):
        print("------------------------------------------")
        print(f"Flight {self.flightCode} report:")
        print(f"- height: {self.height}")
        print(f"- latitude: {self.latitude}")
        print(f"- longitude: {self.longitude}")
        print("------------------------------------------")
