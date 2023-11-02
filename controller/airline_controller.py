from model.airline import Airline

class AirlineController():

	def __init__(self) -> None:
		self._airlines : dict[str , Airline] = {} 
		
	def create_airline(self, name : str ) -> None :
		self._airlines[name] = Airline( name )

	def get_airlines(self) -> dict[str : int]:
		ans = {}
		for value in self._airlines.values():
			ans[value.getName()] =  value.getAmountFlights()
		return ans
	
	def get_airline_flights(self, name : str) -> dict[str : dict[str : None]]:
		return self._airlines[name].getFlights()

	def delete_airline(self, name : str ) -> None :
		if name in self._airlines:
			del self._airlines[name]

	def delete_airline_flight(self, name_airline : str, flightId : str ) -> None :
		self._airlines[name_airline].deleteFlight(flightId)

if __name__ == "__main__":
	pass
