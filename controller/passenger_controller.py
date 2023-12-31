from controller.airport_controller import AirportController
from view.errorMessage import errorMessage            

import datetime
import requests
import json

class PassengerController():

	def __init__( self ):
		self._data = AirportController()

	def create_passager( self, cedula: str, name: str, surname: str, birthDate: str, genre: str, address: str, phoneNumber: str, email: str, nationality : str, medicalInfo : str, luggageAmount : str) -> None:
		if cedula == "" or name == "" or surname == "" or address == "" or phoneNumber == "" or email == "" or nationality == "":
			errorMessage( "Error: No hay la sufiente informacion para registrarse.")
			return
		self._data.create_passager( cedula, name, surname, birthDate, genre, address, phoneNumber, email, nationality, medicalInfo, luggageAmount)

	def assing_passenger_to_flight(self, passengerCedula : str, idFlight : str) -> None:
		if passengerCedula == "" :
			errorMessage("Error: Se necesita la cedula del usuario para reservar el vuelo")
			return
		elif idFlight is None or idFlight == "":
			errorMessage("Error: Se necesita el codigo del vuelo para reservar")
			return
		self._data.assign_passenger_to_flight(passengerCedula, idFlight)

	def get_airports(self):
		res = []
		tmp = self._data.get_airports()
		for airport in tmp :
			res.append( airport[0] )
		return res

	def get_flight_filter(self, origin : str = None, destiny : str = None, date : datetime.date = None):
		fun = lambda f : (f.getOrigin() == origin or origin is None ) and (f.getDestiny() == destiny or destiny is None ) and (f.getDate() == date or date is None) and ( not f.isInAir())
		flights = self._data.get_flights_generic("client", "", fun )
		ans = [ tuple(list(f[0:5]) +  list(f[6 : 8])) for f in flights]
		return ans
	
	def get_country_data(self, country_name):
		url = f"https://restcountries.com/v3.1/name/{country_name}"
		response = requests.get(url)
		
		if response.status_code == 200:
			data = json.loads(response.text)
			return data[0]
		else:
			return None
