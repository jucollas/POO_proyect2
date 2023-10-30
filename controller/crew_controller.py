import model.connections as connect
from model.crew import Crew
from view.errorMessage import errorMessage

def get_crewMembers() -> list[(str)] :
	res = []
	for member in connect.crewMembers.values() :
		res.append( ( member.getCedula(), member.getName(), member.getSurname(), member.getBirthDate(), member.getGenre(), member.getAddress(), member.getPhoneNumber(), member.getEmail(), member.getJobPosition(), member.getDailyWorkingHours(), member.getYearsExperience() ) );
	return res;

def get_crew_id() -> list[str] :
	res = []
	for member in connect.crewMembers.values() :
		res.append( member.getCedula() );
	return res;

def create_crewMember( miembro : Crew ) ->None :
	if ( miembro is None ):
		return;
	elif ( miembro.getCedula() in connect.crewMembers ):
		errorMessage( "Error: la cedula %s ya esta utilizada por un miembro de la tripulacion." % ( miembro.getCedula() ) )
		return;
	connect.crewMembers[miembro.getCedula()] = miembro;

def delete_crewMember( cedula : str ) -> None :
	if ( cedula not in connect.crewMembers ):
		errorMessage( "Error: no existe ningun miembro de la tripulacion con cedula %s." % ( cedula ) )
		return;
	del connect.crewMembers[cedula]