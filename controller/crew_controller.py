from controller.airport_controller import AirportController
from view.errorMessage import errorMessage

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

	def create_crewMember(self, cedula: str, name: str, surname: str, birthDate: str, genre: str, address: str, phoneNumber: str, email: str, jobPosition: str, dailyWorkingHours: int, yearsExperience: int ) ->None :
		self._data.create_crew( cedula, name, surname, birthDate, genre, address, phoneNumber, email, jobPosition, dailyWorkingHours, yearsExperience )

	def delete_crewMember(self, cedula : str ) -> None :
		self._data.delete_crew( cedula)