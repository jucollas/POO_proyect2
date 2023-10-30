from model.helicopter import Helicopter
from model.plane import Plane
from model.jet import Jet
from model.aircraft import Aircraft
from model.person import Person

class AircraftFactory:
    @staticmethod
    def create_aircraft(aircraft_type : str, N_number : str, brand : str, model : str, yearProduction : str, abilityPass : int, speedMax : int, autonomy : int, nRotors : int = None, liftingCapacity : int = None, specificUse : str = None, owner : Person  = None, heightMax : int = None, nEngines : int = None, category : str = None) -> Aircraft:
        aircraft = Aircraft(N_number, brand, model, yearProduction, abilityPass, speedMax, autonomy)
        if aircraft_type == "helicopter":
            if ( nRotors == None or liftingCapacity == None or specificUse == None ):
                raise Exception( "Error: The arguments passed to 'create_aircraft' weren't enough to make a %s\n" % ( aircraft_type ) )
            return Helicopter( aircraft, nRotors, liftingCapacity, specificUse)
        elif aircraft_type == "plane":
            if ( heightMax == None or nEngines == None or category == None ):
                raise Exception( "Error: The arguments passed to 'create_aircraft' weren't enough to make a %s\n" % ( aircraft_type ) )
            return Plane( aircraft, heightMax, nEngines, category)
        elif aircraft_type == "jet":
            if ( owner == None ):
                raise Exception( "Error: The arguments passed to 'create_aircraft' weren't enough to make a %s\n" % ( aircraft_type ) )
            return Jet( aircraft, owner)
        else:
            raise ValueError("Invalid aircraft type")

if __name__ == "__main__":
    plane = AircraftFactory.create_aircraft( "plane", "tango-00", "mitsubishi", "airbus", "100A.C", 10, 20, 10000, heightMax = 840, nEngines = 2, category = "comercial" );
    print( plane );
    heli = AircraftFactory.create_aircraft( "helicopter", "tango-00", "mitsubishi", "airbus", "100A.C", 10, 20, 10000, heightMax = 840, nRotors = 1, liftingCapacity = 200, specificUse = "rescate" );
    print( heli );
    p = Person( "1110101", "oscar", "vargas", "hoy", "macho", "en tu casa", "0135462013", "hola@gmail.com" );
    jet = AircraftFactory.create_aircraft( "jet", "tango-00", "mitsubishi", "airbus", "100A.C", 10, 20, 10000, owner = p );
    print ( jet )