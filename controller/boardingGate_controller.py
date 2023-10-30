import model.connections as connect
from model.control_tower import ControlTower
from view.errorMessage import errorMessage


def get_cities() -> list[str] :
	res = []
	for city in connect.cities.values():
		res.append( city.getCity() );
	return res;

def get_boardingGates( city : str ) :
	if city is None:
		return {};
	res = [];
	boardingGates = connect.cities[city].getBoardingGates();
	for gate in boardingGates.values():
		history = []
		for h in gate.getHistory():
			history.append( h.getFlightCode() );
		res.append( ( gate.getIdentification(), gate.getLocation(), gate.getInGate(), history  ) );
	return res;

def create_boardingGate( city : str, ident : str, loc : str ) -> None :
	if ident in connect.cities[city].getBoardingGates() : 
		errorMessage( "Error: The id %s is already taken in the city %s." % ( ident, city ) );
	else:
		connect.cities[city].addGate( ident, loc );

def delete_boardingGate( city : str, id : str ) -> None :
	connect.cities[city].deleteGate( id );

def get_deletable_gates( city : str ) -> list[str] :
	res = []
	boardingGates = connect.cities[city].getBoardingGates();
	for gate in boardingGates.values():
		if gate.isAvailable():
			res.append( gate.getIdentification() );
	return res;
