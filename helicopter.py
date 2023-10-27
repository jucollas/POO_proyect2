from aircraft import Aircraft

class Helicopter(Aircraft):
    def __init__(self, aircraft : Aircraft, nRotors : int, liftingCapacity : int, specificUse : str) -> 'Helicopter':
        super().__init__(aircraft.getN_number(), aircraft.getBrand(), aircraft.getModel(), aircraft.getYearProduction(), aircraft.getStatus(), aircraft.getAbilityPass(), aircraft.getSpeedMax(), aircraft.getAutonomy())
        self._nRotors = nRotors
        self._liftingCapacity = liftingCapacity
        self._specificUse = specificUse

    def getNRotors(self) -> int: 
        return self._nRotors

    def getLiftingCapacity(self) -> int:
        return self._liftingCapacity

    def getSpecificUse(self) -> int:
        return self._specificUse

    def setNRotors(self, nRotors) -> None:
        self._nRotors = nRotors

    def setLiftingCapacity(self, liftingCapacity) -> None:
        self._liftingCapacity = liftingCapacity

    def setSpecificUse(self, specificUse) -> None:
        self._specificUse = specificUse

    def printInfo(self) -> None:
        print("----- HELICOPTER -----")
        super().printInfo()
        print("N Rotors:", self.getNRotors())
        print("Lifting Capacity:", self.getLiftingCapacity())
        print("Specific Use:", self.getSpecificUse())
