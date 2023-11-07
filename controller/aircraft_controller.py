from model.aircraft_factory import AircraftFactory
from model.aircraft import Aircraft
from model.person import Person
from controller.airport_controller import AirportController
from view.errorMessage import errorMessage
import datetime

class AircraftController():

	def __init__(self) -> None:
		self._data = AirportController()
		
	def get_aircrafts(self) :
		return self._data.get_aircrafts();

	def create_aircraft(self, aircraft_type : str, N_number : str, brand : str, model : str, yearProduction : str, abilityPass : int, speedMax : int, autonomy : int, nRotors : int = None, liftingCapacity : int = None, specificUse : str = None, cedula : str = None, name : str = None, surname : str = None, birthDate : datetime.date = None, genre : str = None, address : str = None, phoneNumber : str = None, email : str = None, heightMax : int = None, nEngines : int = None, category : str = None) -> None :
		if ( N_number == "" or brand == "" or model == ""):
			errorMessage("Error: No hay datos suficientes para crear la aeronave")
			return
		if aircraft_type == "Helicoptero":
			aircraft_type = "helicopter"
		elif aircraft_type == "Avion":
			aircraft_type = "plane"
		elif aircraft_type == "Jet":
			if cedula == "" or name == "" or surname == "" or address == "" or phoneNumber == "" or email == "":
				errorMessage("Error: Se necesita la informacion de propietario")
				return
			aircraft_type = "jet"
		aircraft = AircraftFactory.create_aircraft( aircraft_type, N_number, brand, model, yearProduction, abilityPass, speedMax, autonomy, nRotors = nRotors, liftingCapacity = liftingCapacity, specificUse = specificUse, owner = Person( cedula, name, surname, birthDate, genre, address, phoneNumber, email ), heightMax = heightMax, nEngines = nEngines, category = category )
		self._data.create_aircraft( aircraft)

	def get_deletable_aircrafts(self) -> list[str] :
		ans = []
		tmp = self._data.get_aircrafts();
		for aircraft in tmp:
			if ( not aircraft[8] and aircraft[7] == 0 ):
				ans.append( aircraft[0] )
		return ans

	def delete_aircraft(self, airId : str ) -> None :
		if airId is None:
			return;
		self._data.delete_aircraft( airId )

	def get_manteinable_aircrafts(self) -> list[str] :
		ans = []
		tmp = self._data.get_aircrafts();
		for aircraft in tmp:
			if ( not aircraft[8] ):
				ans.append( aircraft[0] )
		return ans

	def get_aircraft_manteinanceInfo(self,  airId : str ) -> None:
		if airId is None:
			return;
		tmp = self._data.get_aircrafts();
		for aircraft in tmp:
			if ( aircraft[0] == airId ):
				return aircraft[9]
		
	def change_manteinance(self, airId : str, manteinance : bool ) -> None :
		if airId is None:
			return;
		self._data.change_manteinance( airId,manteinance )
