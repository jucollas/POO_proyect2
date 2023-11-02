from controller.airport_controller import AirportController

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
		if city is None:
			return;
		self._data.create_boardingGate( ident, loc )

	def delete_boardingGate( self, city : str, ide: str ) -> None :
		if city is None:
			return;
		self._data.delete_boardingGate( ide );

	def get_deletable_gates( self, city : str ) -> list[str] :
		if city is None:
			return [];
		res = []
		tmp = self._data.get_boardingGates();
		for index in range(len(tmp)):
			if ( tmp[index][2] is None ):
				res.append( tmp[index][0] )
		return res;
