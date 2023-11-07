from controller.airport_controller import AirportController
from view.errorMessage import errorMessage


class AirlineController():

	def __init__( self ):
		self._data = AirportController()
		
	def create_airline(self, name : str ) -> None :
		if name is None or name == "":
			errorMessage( "Error: Se necesita un nombre para crear la aerolinea")
			return
		self._data.create_airline( name )

	def get_airlines(self):
		return self._data.get_airlines()

	def get_deletable_airlines( self ):
		res = []
		tmp = self._data.get_airlines()
		for i in range( len(tmp)):
			if ( tmp[i][1] == 0 ):
				res.append( tmp[i][0] )
		return res

	def delete_airline(self, name : str ) -> None :
		if name is None or name == "":
			return ;
		self._data.delete_airline( name );

if __name__ == "__main__":
	pass
