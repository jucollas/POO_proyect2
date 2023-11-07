from controller.airport_controller import AirportController
from view.errorMessage import errorMessage



class ControlTower_controller():
	
	def __init__( self ):
		self._data = AirportController();

	def create_airport( self, name : str ) -> None:
		if name is None or name == "":
			errorMessage( "Error: Se necesita el nombre de la cuidad para crear el aeropuerto")
			return
		self._data.create_airport( name )

	def get_airports(self) :
		return self._data.get_airports()

	def get_deletable_airports( self ):
		res = [];
		tmp = self._data.get_airports();
		for index in range(len(tmp)):
			if ( tmp[index][1] == 0 ):
				res.append( tmp[index][0] );
		return res;

	def delete_airport( self, name : str  ) -> None :
		if name is None or name == "":
			return;
		self._data.delete_airport( name );