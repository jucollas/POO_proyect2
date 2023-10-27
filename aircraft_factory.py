from helicopter import Helicopter
from plane import Plane
from jet import Jet
from aircraft import Aircraft
from person import Person

class AircraftFactory:
    @staticmethod
    def create_aircraft(aircraft_type : str, N_numer : str, brand : str, model : str, yearProduction : str, status : str, abilityPass : int, speedMax : int, autonomy : int, nRotors : int = None, liftingCapacity : int = None, specificUse : str = None, owner : Person  = None, heightMax : int = None, nEngines : int = None, category : str = None) -> Aircraft:
        Aircraft(N_numer, brand, model, yearProduction, status, abilityPass, speedMax, autonomy)
        if aircraft_type == "helicopter":
            return Helicopter(Aircraft, nRotors, liftingCapacity, specificUse)
        elif aircraft_type == "plane":
            return Plane(Aircraft, heightMax, nEngines, category)
        elif aircraft_type == "jet":
            return Jet(Aircraft, owner)
        else:
            raise ValueError("Invalid aircraft type")