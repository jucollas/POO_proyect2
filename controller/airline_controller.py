from model.airline import Airline
import model.connections as connect
from model.airline import Airline

def create_airline( name : str ) -> None :
	connect.airlines[name] = Airline( name );

def get_airlines():
	res = {}
	for value in connect.airlines.values():
		res[value.getName()] =  value.getAmountFlights();
	return res;

def delete_airline( name  ) -> None :
	if name is not None:
		del connect.airlines[name]



if __name__ == "__main__":
	pass
