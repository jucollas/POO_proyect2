from model.control_tower import ControlTower
import model.connections as connect

def create_airport( name : str ) -> None:
	connect.cities[name] = ControlTower( name );

def get_airports() -> list[str]:
	res = [];
	for airport in connect.cities.values():
		res.append( airport.getCity() );
	return res

def delete_airport( name : str  ) -> None :
	if ( name is not None ):
		del connect.cities[name];