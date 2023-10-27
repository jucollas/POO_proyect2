from aircraft import Aircraft

class Plane(Aircraft):
    def __init__(self, aircraft : Aircraft, heightMax : int, nEngines : int, category : str):
        super().__init__(aircraft.getN_number(), aircraft.getBrand(), aircraft.getModel(), aircraft.getYearProduction(), aircraft.getStatus(), aircraft.getAbilityPass(), aircraft.getSpeedMax(), aircraft.getAutonomy())
        self._heightMax = heightMax
        self._nEngines = nEngines
        self._category = category

    def getHeightMax(self):
        return self._heightMax

    def getNEngines(self):
        return self._nEngines

    def getCategory(self):
        return self._category

    def setHeightMax(self, heightMax):
        self._heightMax = heightMax

    def setNEngines(self, nEngines):
        self._nEngines = nEngines

    def setCategory(self, category):
        self._category = category

    def printInfo(self):
        print("----- PLANE -----")
        super().printInfo()
        print("Height Max:", self.getHeightMax())
        print("N Engines:", self.getNEngines())
        print("Category:", self.getCategory())
