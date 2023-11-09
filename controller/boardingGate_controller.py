from controller.airport_controller import AirportController
from view.errorMessage import errorMessage

class BoardingGate_Controller():

	def __init__( self ):
		self._data = AirportController();

	def get_cities( self ) -> list[str] :
		tmp = self._data.get_airports();
		res = [ a[0] for a in tmp ];
		return res;

	def get_boardingGates( self, city : str ) :
		if city is None:
			return [];
		return self._data.get_boardingGates( city );

	def create_boardingGate( self, city : str, ident : str, loc : str ) -> None :
		if city is None or ident is None or ident == "" or loc == "":
			errorMessage( "Error: No hay informacion insuficiente para crear puerta de abordaje" )
			return;
		self._data.create_boardingGate( city, ident, loc )

	def delete_boardingGate( self, city : str, ide: str ) -> None :
		if city is None or ide is None or ide == "":
			return;
		self._data.delete_boardingGate( city, ide );

	def get_deletable_gates( self, city : str ) -> list[str] :
		if city is None:
			return [];
		res = []
		tmp = self._data.get_boardingGates(city);
		for index in range(len(tmp)):
			if ( tmp[index][2] is None ):
				res.append( tmp[index][0] )
		return res;
