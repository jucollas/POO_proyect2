MaxFlightsPerAircraft = 3

class Aircraft:

    def __init__(self, N_numer : str, brand : str, model : str, yearProduction : str, abilityPass : int, speedMax : int, autonomy : int) -> None:
        self._N_number = N_numer
        self._brand = brand
        self._model = model
        self._yearProduction = yearProduction
        self._abilityPass = abilityPass
        self._speedMax = speedMax
        self._autonomy = autonomy;
        self._asociatedFlights : int = 0
        self._inFlight : bool = False
        self._manteinance : bool = False

    # gets
    
    def getN_number( self ) -> str :
        return self._N_number;

    def getBrand(self) -> str :
        return self._brand
    
    def getModel(self) -> str :
        return self._model

    def getYearProduction(self) -> str :
        return self._yearProduction
    
    def getAbilityPass(self) -> int :
        return self._abilityPass
    
    def getSpeedMax(self) -> int :
        return self._speedMax
    
    def getAutonomy(self) -> int :
        return self._autonomy
    
    def getAsociatedFlights(self) -> int :
        return self._asociatedFlights
    
    def isInFlight(self) -> bool :
        return self._inFlight
    
    def inManteinance(self) -> bool :
        return self._manteinance
    
    #sets

    def setBrand(self, brand) -> None :
        self._brand = brand

    def setModel(self, model) -> None :
        self._model = model

    def setYearProduction(self, yearProduction) -> None :
        self._yearProduction = yearProduction

    def setAbilityPass(self, abilityPass ) -> None :
        self._abilityPass = abilityPass

    def setSpeedMax(self, speedMax) -> None :
        self._speedMax = speedMax

    def setAutonomy(self, autonomy) -> None :
        self._autonomy = autonomy

    #functions

    def canAssignFlight(self) -> bool :
        return MaxFlightsPerAircraft > self.getAsociatedFlights()
    
    def assignFlight(self) -> None :
        if self.canAssignFlight():
            self._asociatedFlights += 1
        else:
            raise Exception( "Error: there are many flights asociated to this aircraft\n" )
        
    def activateFlight(self) -> None :
        if self._inFlight:
            raise Exception( "Error: we are already in flight." )            
        else:
            self._inFlight = True

    def deactivateFlight(self) -> None :
        if not self._inFlight:
            raise Exception( "Error: we are not already in flight." )          
        else:
            self._inFlight = False
            self._asociatedFlights -= 1

    def putInManteinance(self) -> None :
        if self.isInFlight() or self.inManteinance():
            raise Exception("Error: unable to put in manteinance.")
        else:
            self._manteinance = True

    def endManteinance(self) -> None :
        if not self.inManteinance():
            raise Exception("Error: already in manteinance")
        else:
            self._manteinance = False

    def __str__(self) -> str :
        tmp = []
        tmp.append("N Number: %s" %(self.getN_number()))
        tmp.append("Model: %s" %(self.getModel()))
        tmp.append("Ability to Passengers: %d" %(self.getAbilityPass()))
        tmp.append("Maximum Speed: %d" %(self.getSpeedMax()))
        tmp.append("Autonomy: %d" %(self.getAutonomy()))
        return ". ".join( tmp );

if __name__ == "__main__":
    av = Aircraft( "tango-00", "boeing", "airbus", "anteayer", 100, 200, 300  );
    print( av );
