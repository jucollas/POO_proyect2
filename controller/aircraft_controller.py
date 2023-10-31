import model.connections as connect
from model.aircraft_factory import AircraftFactory
from model.aircraft import Aircraft
from model.jet import Jet
from model.helicopter import Helicopter
from model.plane import Plane
from model.person import Person
from view.errorMessage import errorMessage


def get_aircrafts() :
	res = []
	for aircraft in connect.aircrafts.values():
		res.append( (aircraft.getN_number(), aircraft.getBrand(), aircraft.getModel(), aircraft.getYearProduction(), str(aircraft.getAbilityPass()), str(aircraft.getSpeedMax()), str(aircraft.getAutonomy()), str(aircraft.getAsociatedFlights()), str(aircraft.isInFlight()), str(aircraft.inManteinance() ))) ;
	return res;

def create_aircraft(aircraft_type : str, N_number : str, brand : str, model : str, yearProduction : str, abilityPass : int, speedMax : int, autonomy : int, nRotors : int, liftingCapacity : int, specificUse : str, owner : Person, heightMax : int, nEngines : int, category : str) -> None :
	if N_number in connect.aircrafts:
		errorMessage( "Error: The serial number %s is already taken." % ( N_number ) );
		return;
	if aircraft_type == "Helicoptero":
		aircraft_type = "helicopter"
	elif aircraft_type == "Avion":
		aircraft_type = "plane"
	elif aircraft_type == "Jet":
		aircraft_type = "jet"
	aircraft = AircraftFactory.create_aircraft( aircraft_type, N_number, brand, model, yearProduction, abilityPass, speedMax, autonomy, nRotors = nRotors, liftingCapacity = liftingCapacity, specificUse = specificUse, owner = owner, heightMax = heightMax, nEngines = nEngines, category = category );
	connect.aircrafts[N_number] = aircraft;

def get_deletable_aircrafts() -> list[str] :
	res = []
	for aircraft in connect.aircrafts.values():
		if ( not aircraft.isInFlight() and aircraft.getAsociatedFlights() == 0 ):
			res.append( aircraft.getN_number() );
	return res

def delete_aircraft( airId : str ) -> None :
	if ( airId is not None ):
		del connect.aircrafts[airId]

def get_manteinable_aircrafts() -> list[str] :
	res = []
	for aircraft in connect.aircrafts.values():
		if ( not aircraft.isInFlight() ):
			res.append( aircraft.getN_number() );
	return res

def get_aircraft_manteinanceInfo( airId : str ) -> None:
	if ( airId is not None ):
		return connect.aircrafts[airId].inManteinance();
def change_manteinance( airId : str, manteinance : bool ) -> None :
	if ( airId is None ):
		return;
	connect.aircrafts[airId].toggleManteinance( manteinance );