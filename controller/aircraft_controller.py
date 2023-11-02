from model.aircraft_factory import AircraftFactory
from model.aircraft import Aircraft
from model.person import Person
from view.errorMessage import errorMessage

class AircraftController:

	def __init__(self) -> None:
		self._aircrafts : dict[str, Aircraft] = {}
		
	def get_aircrafts(self) :
		ans = {}
		for aircraft in self._aircrafts.values():
			ans[aircraft.getN_number()] = vars(aircraft)
		return ans

	def create_aircraft(self, aircraft_type : str, N_number : str, brand : str, model : str, yearProduction : str, abilityPass : int, speedMax : int, autonomy : int, nRotors : int = None, liftingCapacity : int = None, specificUse : str = None, owner : Person  = None, heightMax : int = None, nEngines : int = None, category : str = None) -> None :

		if N_number in self._aircrafts:
			errorMessage( "Error: The serial number %s is already taken." % ( N_number ) )
			return
		if aircraft_type == "Helicoptero":
			aircraft_type = "helicopter"
		elif aircraft_type == "Avion":
			aircraft_type = "plane"
		elif aircraft_type == "Jet":
			aircraft_type = "jet"
		aircraft = AircraftFactory.create_aircraft( aircraft_type, N_number, brand, model, yearProduction, abilityPass, speedMax, autonomy, nRotors = nRotors, liftingCapacity = liftingCapacity, specificUse = specificUse, owner = owner, heightMax = heightMax, nEngines = nEngines, category = category )
		self._aircrafts[N_number] = aircraft

	def get_deletable_aircrafts(self) -> list[str] :
		ans = []
		for aircraft in self._aircrafts.values():
			if ( not aircraft.isInFlight() and aircraft.getAsociatedFlights() == 0 ):
				ans.append( aircraft.getN_number() )
		return ans

	def delete_aircraft(self, airId : str ) -> None :
		if ( airId in self._aircrafts ):
			del self._aircrafts[airId]

	def get_manteinable_aircrafts(self) -> list[str] :
		ans = []
		for aircraft in self._aircrafts.values():
			if ( not aircraft.isInFlight() ):
				ans.append( aircraft.getN_number() )
		return ans

	def get_aircraft_manteinanceInfo(self,  airId : str ) -> None:
		if ( airId is not None ):
			return self._aircrafts[airId].inManteinance()
		
	def change_manteinance(self, airId : str, manteinance : bool ) -> None :
		if (not airId in self._aircrafts ):
			return
		self._aircrafts[airId].toggleManteinance( manteinance )
