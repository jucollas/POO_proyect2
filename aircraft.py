MaxFlightsPerAircraft = 3

class Aircraft:

    def __init__(self, N_numer : str, brand : str, model : str, yearProduction : str, status : str, abilityPass : int, speedMax : int, autonomy : int) -> None:
        self._N_number = N_numer
        self._brand = brand
        self._model = model
        self._yearProduction = yearProduction
        self._status = status
        self._abilityPass = abilityPass
        self._speedMax = speedMax
        self._autonomy = autonomy
        self._asociatedFlights : int = 0
        self._inFlight : bool = False
        self._manteinance : bool = False

    # gets
    
    def getN_number(self):
        return self._N_number

    def getBrand(self):
        return self._brand
    
    def getModel(self):
        return self._model

    def getYearProduction(self):
        return self._yearProduction
        
    def getStatus(self):
        return self._status
    
    def getAbilityPass(self):
        return self._abilityPass
    
    def getSpeedMax(self):
        return self._speedMax
    
    def getAutonomy(self):
        return self._autonomy
    
    def getAsociatedFlights(self):
        return self._asociatedFlights
    
    def isInFlight(self):
        return self._inFlight
    
    def inManteinance(self):
        return self._manteinance
    
    #sets

    def setBrand(self, brand):
        self._brand = brand

    def setModel(self, model):
        self._model = model

    def setYearProduction(self, yearProduction):
        self._yearProduction = yearProduction

    def setStatus(self, status ):
        self._status = status

    def setAbilityPass(self, abilityPass ):
        self._abilityPass = abilityPass

    def setSpeedMax(self, speedMax):
        self._speedMax = speedMax

    def setAutonomy(self, autonomy):
        self._autonomy = autonomy

    #functions

    def canAssignFlight(self):
        return MaxFlightsPerAircraft > self.getAsociatedFlights()
    
    def assignFlight(self):
        if self.canAssignFlight():
            self._asociatedFlights += 1
        else:
            raise Exception( "Error: there are many flights asociated to this aircraft\n" )
        
    def activateFlight(self):
        if self._inFlight:
            raise Exception( "Error: we are already in flight." )            
        else:
            self._inFlight = True

    def deactivateFlight(self):
        if not self._inFlight:
            raise Exception( "Error: we are not already in flight." )          
        else:
            self._inFlight = False
            self._asociatedFlights -= 1

    def putInManteinance(self):
        if self.isInFlight() or self.inManteinance():
            raise Exception("Error: unable to put in manteinance.")
        else:
            self._manteinance = True

    def endManteinance(self):
        if not self.inManteinance():
            raise Exception("Error: already in manteinance")
        else:
            self._manteinance = False

    def printInfo(self):
        print("N Number: %s" %(self.getN_number()))
        print("Brand: %s" %(self.getBrand()))
        print("Model: %s" %(self.getModel()))
        print("Year of Production: %d" %(self.getYearProduction()))
        print("Status: %d" %(self.getStatus()))
        print("Ability to Passengers: %d" %(self.getAbilityPass()))
        print("Maximum Speed: %d" %(self.getSpeedMax()))
        print("Autonomy: %d" %(self.getAutonomy()))