from model.aircraft import Aircraft

class Helicopter(Aircraft):
    def __init__(self, aircraft : Aircraft, nRotors : int, liftingCapacity : int, specificUse : str) -> 'Helicopter':
        super().__init__(aircraft.getN_number(), aircraft.getBrand(), aircraft.getModel(), aircraft.getYearProduction(), aircraft.getAbilityPass(), aircraft.getSpeedMax(), aircraft.getAutonomy())
        self._nRotors = nRotors
        self._liftingCapacity = liftingCapacity
        self._specificUse = specificUse

    # get

    def getNRotors(self) -> int: 
        return self._nRotors

    def getLiftingCapacity(self) -> int:
        return self._liftingCapacity

    def getSpecificUse(self) -> int:
        return self._specificUse

    # set 
    
    def setNRotors(self, nRotors : int ) -> None:
        self._nRotors = nRotors

    def setLiftingCapacity(self, liftingCapacity : int ) -> None:
        self._liftingCapacity = liftingCapacity

    def setSpecificUse(self, specificUse : str ) -> None:
        self._specificUse = specificUse

    def __str__(self) -> str :
        tmp = [ super().__str__() ]
        tmp.append("N Rotors: %d" % ( self.getNRotors()) )
        tmp.append("Lifting Capacity: %d" % ( self.getLiftingCapacity()) )
        tmp.append("Specific Use: %s" %  (self.getSpecificUse()) )
        return ". ".join( tmp )

if __name__ == "__main__":
    av = Aircraft( "tango-00", "boeing", "airbus", "anteayer", 100, 200, 300  );
    heli = Helicopter( av, 2, 50, "hotel" );
    print( heli );
