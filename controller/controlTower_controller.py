from controller.airport_controller import AirportController

def ControlTowerController():
	
	def __init__ ( self ):
		self._data = AirportController();

	def create_airport( self, name : str ) -> None:
		self._data.create_airport( name )

	def get_airports(self) -> list[str]:
		return self._data.get_airports()

	def get_deletable_airports( self ):
		res = [];
		tmp = self._data.get_airports();
		for index in range(len(tmp)):
			if ( tmp[index][1] == 0 ):
				res.append( tmp[0] );
		return res;

	def delete_airport( self, name : str  ) -> None :
		self._data.delete_airport( name );