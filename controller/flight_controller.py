from controller.airport_controller import AirportController
from view.errorMessage import errorMessage
import datetime

class FlightController():

	def __init__( self ) :
		self._data = AirportController();

	def get_airlines( self ):
		res = []
		tmp = self._data.get_airlines();
		for airline in tmp:
			res.append( airline[0] )
		return res;

	def get_airports( self ):
		res = []
		tmp = self._data.get_airports()
		for airport in tmp :
			res.append( airport[0] )
		return res;

	def get_airline_flights( self, airline : str ) :
		if airline is None:
			return [];
		return self._data.get_flights_generic( "airline", airline )

	def get_airport_flights( self, airport : str ) :
		if airport is None:
			return []
		return self._data.get_flights_generic( "airport", airport )
	
	def get_messages_flight(self, flight) -> list[tuple]:
		if flight is None:
			return []
		return self._data.get_messages_flight(flight)

	def get_airline_flight_id( self, airline : str ):
		if airline is None:
			return [];
		return [ f[0] for f in self._data.get_flights_generic( "airline", airline ) ]

	def get_airport_flight_id( self, airport : str ):
		if airport is None:
			return [];
		return [ f[0] for f in self._data.get_flights_generic( "airport", airport ) ]


	def get_posible_aircraft(self, origin : str):
		res = []
		tmp = self._data.get_aircrafts();
		for air in tmp : 
			if ( air[11] and not origin in air[10] ):
				res.append( "|".join( [air[0], " - ".join( [air[1], air[2], str(air[4]), str(air[5]), str(air[6])] )] ));
		return res

	def get_crew(self):
		res = []
		tmp = self._data.get_crews();
		for c in tmp:
			res.append( "|".join( [c[0], " - ".join( [str(c[1]), str(c[2]), str(c[8]), str(c[9]), str(c[10])] ) ] ));
		return res

	def create_flight( self, airline : str, aircraft : str, flightCode : str, date : datetime.date, origin : str, destiny : str, crew : list[str]  ):
		if airline is None or aircraft is None or flightCode == "" or origin is None or destiny is None or len(crew) == 0:
			errorMessage( "Error: no hay suficientes datos para crear el vuelo" )
			return
		elif not self._data.there_pilot(crew):
			errorMessage( "Error: Se necesita en la tripulacion por lo menos un piloto" )
			return
		self._data.create_flight( airline, aircraft, flightCode, date, origin, destiny, crew )

	def cancel_flight( self, airline : str, flightId : str ) -> None :
		if airline is None or flightId is None:
			return;
		self._data.cancel_flight( airline, flightId )

	def start_flight( self, airline : str, flightId : str ) -> None :
		if airline is None or flightId is None:
			return;
		self._data.start_flight( airline, flightId )

	def get_startable_flights( self, airline : str ):
		if ( airline is None ):
			return [];
		return [ f[0] for f in self._data.get_flights_generic( "airline", airline, fun = lambda f : f.canActivate() )]

	def get_takeOff_flights( self, airport : str ):
		if ( airport is None ):
			return [];
		return [ f[0] for f in self._data.get_flights_generic( "airport", airport, fun = lambda f : f.getOrigin() == airport and not f.isInAir() )]

	def get_landing_flights( self, airport : str ):
		if ( airport is None ):
			return [];
		return [ f[0] for f in self._data.get_flights_generic( "airport", airport, fun = lambda f : f.isInAir() and f.getDestiny() == airport )]

	def get_finishing_flights( self, airport : str ):
		if ( airport is None ):
			return [];
		return [ f[0] for f in self._data.get_flights_generic( "airport", airport, fun = lambda f : f.isActive() and not f.isInAir() and f.getDestiny() == airport )]

	def get_continue_flights( self, airport : str ):
		if ( airport is None ):
			return [];
		return [ f[0] for f in self._data.get_flights_generic( "airport", airport, fun = lambda f : f.isInAir() and f.getDestiny() != airport )]

	def takeOff_flight( self, airport : str, flight : str ) :
		if airport is None or flight is None:
			return;
		self._data.takeOff_flight( airport, flight )

	def land_flight( self, airport : str, flight : str ) :
		if airport is None or flight is None:
			return;
		self._data.land_flight( airport, flight )

	def end_flight( self, airport : str, flight : str ) :
		if airport is None or flight is None:
			return;
		self._data.end_flight( airport, flight )

	def continue_flight( self, airport : str, flight : str ) :
		if airport is None or flight is None:
			return;
		self._data.continue_flight( airport, flight )

	def notifyFlights(self, flight, airport) -> str:
		if airport is None or flight is None:
			return;
		ans = self._data.notifyFlights(flight, airport)
		return ans
		

