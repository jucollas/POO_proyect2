from model.person import Person
from controller.aircraft_controller import AircraftController
from controller.airline_controller import AirlineController
from controller.controlTower_controller import ControlTower_controller
from controller.boardingGate_controller import BoardingGate_Controller
from controller.crew_controller import CrewController
from controller.flight_controller import FlightController

import datetime

_controllerAircraft = AircraftController()
_controllerAirline = AirlineController()
_controllerCT = ControlTower_controller()
_controllerBC = BoardingGate_Controller()
_controllerCrew = CrewController()
_controllerFlight = FlightController()

class loandigData:

    ## singelton ##

    _instance = None

    def __new__(cls) -> 'loandigData':
        if cls._instance is None:
            cls._instance = super(loandigData, cls).__new__(cls)
            cls._instance._init_loandigData()
        return cls._instance

    def _init_loandigData(self) -> None:
        self._loandig = False

    def data_default(self) -> None:
        if not self._loandig:

            self._loandig = True

            #### Aircraft ####

            _controllerAircraft.create_aircraft( "plane", "tango-00", "mitsubishi", "airbus", "100A.C", 10, 20, 10000, heightMax = 840, nEngines = 2, category = "comercial" );

            _controllerAircraft.create_aircraft( "helicopter", "tango-01", "mitsubishi", "airbus", "100A.C", 10, 20, 10000, heightMax = 840, nRotors = 1, liftingCapacity = 200, specificUse = "rescate" )

            _controllerAircraft.create_aircraft( "jet", "tango-02", "mitsubishi", "airbus", "100A.C", 10, 20, 10000, cedula = "1110101", name = "oscar" , surname = "vargas", birthDate = 'today', genre = "macho", address = "en tu casa", phoneNumber = "0135462013", email = "hola@gmail.com")

            #### Airline ####

            _controllerAirline.create_airline('Avianca')
            _controllerAirline.create_airline('Viva')

            ### Airport ###

            _controllerCT.create_airport('Cali')
            _controllerCT.create_airport('Bogota')
            _controllerCT.create_airport('Cartagena')

            ### Boardig Gate ###

            _controllerBC.create_boardingGate('Cali', 'A0', 'Norte')
            _controllerBC.create_boardingGate('Cali', 'A1', 'Norte')
            _controllerBC.create_boardingGate('Cali', 'A2', 'Norte')
            _controllerBC.create_boardingGate('Bogota', 'A0', 'Sur')
            _controllerBC.create_boardingGate('Bogota', 'A1', 'Norte')
            _controllerBC.create_boardingGate('Bogota', 'A2', 'Oeste')
            _controllerBC.create_boardingGate('Cartagena', 'A0', 'Norte')
            _controllerBC.create_boardingGate('Cartagena', 'A1', 'Norte')
            _controllerBC.create_boardingGate('Cartagena', 'A2', 'Norte')

            ### Crew ####

            data = datetime.date(2023,11,6)

            _controllerCrew.create_crewMember("741852963", "Sara", "Salazar", data, 'Femenino', 'Cr 12 N 8-22', '32314154', 'sara@gmail.com', 'Piloto', 10, 20 )
            _controllerCrew.create_crewMember("85214567", "Santiago", "Salazar", data, 'Masculino', 'Cr 12 N 8-22', '32314154', 'sara@gmail.com', 'Piloto', 10, 20 )
            _controllerCrew.create_crewMember("741852444", "Camila", "Salazar", data, 'Femenino', 'Cr 12 N 8-22', '32314154', 'sara@gmail.com', 'Piloto', 10, 20 )

            ### Flight ###

            _controllerFlight.create_flight('Viva', 'tango-00', 'AV000', data, 'Cali', 'Bogota',["741852963", "85214567", "741852444"])
            _controllerFlight.create_flight('Avianca', 'tango-00', 'AV001', data, 'Bogota', 'Cali',["741852963", "85214567", "741852444"])
            _controllerFlight.create_flight('Viva', 'tango-01', 'AV002', data, 'Cali', 'Cartagena',["741852963", "85214567", "741852444"])
            _controllerFlight.create_flight('Avianca', 'tango-02', 'AV003', data, 'Bogota', 'Cartagena',["741852963", "85214567", "741852444"])
