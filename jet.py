from aircraft import Aircraft
from person import Person

class Jet(Aircraft):
    def __init__(self, aircraft : Aircraft, owner : Person):
        super().__init__(aircraft.getN_number(), aircraft.getBrand(), aircraft.getModel(), aircraft.getYearProduction(), aircraft.getStatus(), aircraft.getAbilityPass(), aircraft.getSpeedMax(), aircraft.getAutonomy())
        self._owner = owner
        self._services = []
        self._frequentDestinations = []

    def getOwner(self):
        return self._owner

    def setOwner(self, owner):
        self._owner = owner

    def addServices(self, serv):
        self._services.append(serv)

    def delServices(self, index):
        if index >= 1 and index <= len(self._services):
            del self._services[index - 1]

    def addDestination(self, des):
        self._frequentDestinations.append(des)

    def delDestination(self, index):
        if index >= 1 and index <= len(self._frequentDestinations):
            del self._frequentDestinations[index - 1]

    def delAllServices(self):
        self._services = []

    def delAllDestinations(self):
        self._frequentDestinations = []

    def printServices(self):
        print("Services:")
        for serv in self._services:
            print("  -", serv)

    def printFrequentDestinations(self):
        print("Frequent Destinations:")
        for dest in self._frequentDestinations:
            print("  -", dest)

    def printInfo(self):
        print("----- JET -----")
        super().printInfo()
        print("Owner:", self._owner.info())
        self.printServices()
        self.printFrequentDestinations()