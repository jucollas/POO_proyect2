from controller.airport_controller import AirportController
from view.errorMessage import errorMessage
import datetime

class CrewController():

	def __init__( self ):
		self._data = AirportController()

	def get_crewMembers(self) -> list[(str)] :
		return self._data.get_crews();

	def get_crew_id(self) -> list[str] :
		res = []
		tmp = self._data.get_crews();
		for member in tmp :
			res.append( member[0] );
		return res;

	def create_crewMember(self, cedula: str, name: str, surname: str, birthDate: datetime.date, genre: str, address: str, phoneNumber: str, email: str, jobPosition: str, dailyWorkingHours: int, yearsExperience: int ) ->None :
		if cedula == "" or name == "" or surname == "" or address == "" or phoneNumber == "" or email == "":
			errorMessage( "Error: No hay la sufiente informacion para crear tripulante.")
			return
		self._data.create_crew( cedula, name, surname, birthDate, genre, address, phoneNumber, email, jobPosition, dailyWorkingHours, yearsExperience )

	def delete_crewMember(self, cedula : str ) -> None :
		if cedula is None or cedula == "":
			return;
		self._data.delete_crew( cedula)