if __name__ == "__main__" or __name__ == "plane":
    from aircraft import Aircraft
else:
    from model.aircraft import Aircraft

class Plane(Aircraft):
    def __init__(self, aircraft : Aircraft, heightMax : int, nEngines : int, category : str):
        super().__init__(aircraft.getN_number(), aircraft.getBrand(), aircraft.getModel(), aircraft.getYearProduction(), aircraft.getAbilityPass(), aircraft.getSpeedMax(), aircraft.getAutonomy())
        self._heightMax = heightMax
        self._nEngines = nEngines
        self._category = category

    def getHeightMax(self) -> int :
        return self._heightMax

    def getNEngines(self) -> int :
        return self._nEngines

    def getCategory(self) -> str :
        return self._category

    def setHeightMax(self, heightMax) -> None :
        self._heightMax = heightMax

    def setNEngines(self, nEngines) -> None :
        self._nEngines = nEngines

    def setCategory(self, category) -> None :
        self._category = category

    def __str__(self) -> str :
        tmp = [ super().__str__() ]
        tmp.append(". N Engines: %d" % (self.getNEngines()))
        tmp.append(". Category: %s" % (self.getCategory()))
        return "".join( tmp );

if __name__ == "__main__":
    av = Aircraft( "tango-00", "boeing", "airbus", "anteayer", 100, 200, 300  );
    pl = Plane( av, 10, 2, "comercial"  );
    print( pl );
