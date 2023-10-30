
airlines = {}
cities = {}
aircrafts = {}
disconnectedFlights = {}


if __name__ == "__main__":
	print( Resources.hola())
	pru = Resources()
	a = Resources.createClass();
	b = Resources.createClass();

	print( id(a) == id(b) )
	print( type( a ) );
	a.airlines["avianca"] = "tuCucha"
	print( b.airlines )