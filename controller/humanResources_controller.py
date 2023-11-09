from controller.airport_controller import AirportController
from view.errorMessage import errorMessage            


class HumanResourceController:
    
    def __init__( self ):
        self._data = AirportController()
        
    def get_all_passenger(self) -> list[tuple[str]]:
        return self._data.get_passenger_generic()
    
    def get_flight_passenger(self, idFlight : str = None) ->  list[tuple[str]]:
        return self._data.get_passenger_generic(idFlight)
    
    def del_passenger(self, cedula: str, flight : str == None) -> None:
        if not flight is None and self._data.isInAir(flight):
            errorMessage("Error: no es puede borrar el pasajero selecionado porque se encuentra en el aire")
            return
        self._data.del_passenger(cedula)

    def get_flights(self) -> list[tuple[str]]:
        flights = self._data.get_flights_generic("client", "")
        ans = [tuple(f[0:4]) for f in flights]
        return ans


    
