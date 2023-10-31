import model.connections as connect
from model.flight import Flight
from view.errorMessage import errorMessage
import datetime
from model.crew import Crew

def get_airlines():
	res = []
	for airline in connect.airlines.values():
		res.append( airline.getName() )
	return res;

def get_airports( ):
	res = []
	for airport in connect.cities.values() :
		res.append( airport.getCity() )
	return res;

def get_flights_fromSource( flights ) :
	res = []
	for f in flights:
		aircraft = f.getAircraft();
		res.append( ( f.getFlightCode(), f.getDate(), f.getOrigin(), f.getDestiny(), aircraft.getN_number(), f.getPassengers(), f.getCrewMates(), f.isInAir() ) );
	return res

def get_airline_flights( airline : str ) :
	if airline is None:
		return []
	return get_flights_fromSource( connect.airlines[airline].getFlights() );

def get_airport_flights( airport : str ) :
	if airport is None:
		return []
	return get_flights_fromSource( connect.cities[airport].getFlights() );

def get_flights_fromSource_id( flights ) :
	res = []
	for f in flights:
		res.append( f.getFlightCode() );
	return res;

def get_airline_flight_id( airline : str ):
	if airline is None:
		return [];
	return get_flights_fromSource_id( connect.airlines[airline].getFlights() );

def get_airport_flight_id( airport : str ):
	if airport is None:
		return [];
	return get_flights_fromSource_id( connect.cities[airport].getFlights() );

def get_posible_aircraft():
	res = []
	for air in connect.aircrafts.values() : 
		if ( air.canAssignFlight() ):
			res.append( "|".join( [air.getN_number(), " - ".join( [air.getBrand(), air.getModel(), str(air.getAbilityPass()), str(air.getSpeedMax()), str(air.getAutonomy())] )] ));
	return res

def get_crew():
	res = []
	for c in connect.crewMembers.values():
		res.append( "|".join( [c.getCedula(), " - ".join( [c.getName(), c.getSurname(), c.getJobPosition(), str(c.getDailyWorkingHours()), str(c.getYearsExperience())] ) ] ));
	return res

def create_flight( airline : str, aircraft : str, flightCode : str, date : datetime.date, origin : str, destiny : str, crew ):
	if False: #mejorar esta condicino
		errorMessage( "Error: el codigo %s ya esta en uso." % ( flightCode ) )
		return;
	f = Flight( connect.aircrafts[aircraft], crew, flightCode, date, origin, destiny );
	connect.airlines[airline].addFlight( f );

def cancel_flight( airline : str, flightId : str ) -> None :
	connect.airlines[airline].deleteFlight( flightId );

def start_flight( airline : str, flightId : str ) -> None :
	connect.airlines[airline].activateFlight( flightId );

def generic_get_flights_fromSource ( flights, fun ):
	res = []
	for f in flights:
		if fun( f ) :
			res.append( f.getFlightCode() );
	return res;


def get_takeOff_flights( airport : str ):
	if ( airport is None ):
		return [];
	return generic_get_flights_fromSource( connect.cities[airport].getFlights(), lambda f : f.getOrigin() == airport and not f.isInAir() );

def get_landing_flights( airport : str ):
	if ( airport is None ):
		return [];
	return generic_get_flights_fromSource( connect.cities[airport].getFlights(), lambda f : f.isInAir() and f.getDestiny() == airport );

def get_finishing_flights( airport : str ):
	if ( airport is None ):
		return [];
	return generic_get_flights_fromSource( connect.cities[airport].getFlights(), lambda f : f.isActive() and not f.isInAir() and f.getDestiny() == airport )

def get_continue_flights( airport : str ):
	if ( airport is None ):
		return [];
	return generic_get_flights_fromSource( connect.cities[airport].getFlights(), lambda f : f.isInAir() and f.getDestiny() != airport )

def takeOff_flight( airport : str, flight : str ) :
	connect.cities[airport].flightTakeOff( flight )

def land_flight( airport : str, flight : str ) :
	connect.cities[airport].flightLand( flight )

def end_flight( airport : str, flight : str ) :
	connect.cities[airport].endFlight( flight )

def continue_flight( airport : str, flight : str ) :
	connect.cities[airport].continueFlight( flight )

