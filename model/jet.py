from model.aircraft import Aircraft
from model.person import Person

class Jet(Aircraft):
    def __init__(self, aircraft : Aircraft, owner : Person):
        super().__init__(aircraft.getN_number(), aircraft.getBrand(), aircraft.getModel(), aircraft.getYearProduction(), aircraft.getAbilityPass(), aircraft.getSpeedMax(), aircraft.getAutonomy())
        self._owner = owner
        self._services = []
        self._frequentDestinations = []

    def getOwner(self) -> Person :
        return self._owner

    def setOwner(self, owner : Person ) -> None :
        self._owner = owner

    def addServices(self, serv) -> None :
        self._services.append(serv)

    def delServices(self, index : int ) -> None :
        if index >= 1 and index <= len(self._services):
            del self._services[index - 1]

    def addDestination(self, des) -> None :
        self._frequentDestinations.append(des)

    def delDestination(self, index : int ) -> None :
        if index >= 1 and index <= len(self._frequentDestinations):
            del self._frequentDestinations[index - 1]

    def delAllServices(self) -> None :
        self._services = []

    def delAllDestinations(self) -> None :
        self._frequentDestinations = []

    def strServices(self):
        tmp = ["Services:", " - ".join( self._services )];
        return " ".join( tmp );

    def strFrequentDestinations(self):
        tmp = ["Frequent Destinations:", " - ".join( self._frequentDestinations ) ];
        return " ".join( tmp );

    def __str__(self) -> str :
        tmp = [ super().__str__() ]
        tmp.append( " ".join( ["Owner:", self._owner.__str__()] ) )
        tmp.append( self.strServices() )
        tmp.append( self.strFrequentDestinations() )
        return ". ".join( tmp );

if __name__ == "__main__":
    av = Aircraft( "tango-00", "boeing", "airbus", "anteayer", 100, 200, 300  );
    man = Person( "1110101", "oscar", "vargas", "hoy", "macho", "en tu casa", "0135462013", "hola@gmail.com" )
    jet = Jet( av, man );
    print( jet );
    jet.addServices( "cuarto para dormir" )
    jet.addServices( "masajes premium" )
    jet.addServices( "discoteca" )
    jet.addDestination( "checoslovaquia" )
    jet.addDestination( "ecuador" )
    jet.addDestination( "argentina" )
    print( jet )
