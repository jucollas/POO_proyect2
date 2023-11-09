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

            _controllerAircraft.create_aircraft("plane", "tango-03", "Boeing", "Boeing 737", "2010", 15, 30, 15000, heightMax = 840, nEngines = 2, category = "comercial" )
            _controllerAircraft.create_aircraft("helicopter", "tango-04", "Airbus", "H125", "2015", 5, 10, 5000, nRotors=2, liftingCapacity=300, specificUse="rescate")
            _controllerAircraft.create_aircraft( "plane", "tango-00", "mitsubishi", "airbus", "2004", 10, 20, 10000, heightMax = 840, nEngines = 2, category = "comercial" )
            _controllerAircraft.create_aircraft( "helicopter", "tango-01", "mitsubishi", "airbus", "2006", 10, 20, 10000, heightMax = 840, nRotors = 1, liftingCapacity = 200, specificUse = "rescate" )

            data = datetime.date(1970,7,6)
            _controllerAircraft.create_aircraft( "jet", "tango-02", "mitsubishi", "airbus", "2020", 10, 20, 10000, cedula = "1110101", name = "oscar" , surname = "vargas", birthDate = data, genre = "Masculino", address = "Cr 14 # 5-33", phoneNumber = "3135462013", email = "oscar@gmail.com")

            #### Airline ####

            _controllerAirline.create_airline('Avianca')
            _controllerAirline.create_airline('Viva')
            _controllerAirline.create_airline('JetBlue')
            _controllerAirline.create_airline('LATAM')

            ### Airport ###

            _controllerCT.create_airport('Cali')
            _controllerCT.create_airport('Bogota')
            _controllerCT.create_airport('Cartagena')
            _controllerCT.create_airport('Medellín')
            _controllerCT.create_airport('Barranquilla')

            ### Boardig Gate ###

            _controllerBC.create_boardingGate('Cali', 'A0', 'Norte')
            _controllerBC.create_boardingGate('Cali', 'A1', 'Norte')
            _controllerBC.create_boardingGate('Cali', 'A2', 'Norte')
            _controllerBC.create_boardingGate('Bogota', 'A0', 'Sur')
            _controllerBC.create_boardingGate('Bogota', 'A1', 'Norte')
            _controllerBC.create_boardingGate('Bogota', 'A2', 'Oeste')
            _controllerBC.create_boardingGate('Cartagena', 'A0', 'Oeste')
            _controllerBC.create_boardingGate('Cartagena', 'A1', 'Este')
            _controllerBC.create_boardingGate('Cartagena', 'A2', 'Norte')
            _controllerBC.create_boardingGate('Medellín', 'A3', 'Este')
            _controllerBC.create_boardingGate('Medellín', 'A4', 'Oeste')
            _controllerBC.create_boardingGate('Barranquilla', 'B0', 'Norte')

            ### Crew ####

            data_sara = datetime.date(1990, 5, 12)
            data_santiago = datetime.date(1985, 8, 21)
            data_camila = datetime.date(1995, 3, 28)
            data_laura = datetime.date(2023, 11, 6)

            _controllerCrew.create_crewMember("741852963", "Sara", "Quintero", data_sara, 'Femenino', 'Cr 12 N 8-22', '32314154', 'sara@gmail.com', 'piloto', 10, 20)
            _controllerCrew.create_crewMember("85214567", "Santiago", "Salazar", data_santiago, 'Masculino', 'Cr 12 N 8-22', '32314154', 'santiago@gmail.com', 'piloto', 10, 20)
            _controllerCrew.create_crewMember("741852444", "Camila", "Sandoval", data_camila, 'Femenino', 'Cr 12 N 8-22', '32314154', 'camila@gmail.com', 'co-piloto', 10, 20)
            _controllerCrew.create_crewMember("963258741", "Laura", "Gómez", data_laura, 'Femenino', 'Cr 7 N 12-33', '321987456', 'laura@gmail.com', 'ingeniero', 8, 15)

            ### Flight ###
            data = datetime.date(2023, 11, 8)


            _controllerFlight.create_flight('Viva', 'tango-00', 'AV000', data, 'Cali', 'Bogota',["741852963", "85214567", "741852444"])
            _controllerFlight.create_flight('Avianca', 'tango-00', 'AV001', data, 'Bogota', 'Cali',["741852963", "85214567", "741852444"])
            _controllerFlight.create_flight('Viva', 'tango-01', 'AV002', data, 'Cali', 'Cartagena',["741852963", "85214567", "741852444"])
            _controllerFlight.create_flight('Avianca', 'tango-02', 'AV003', data, 'Bogota', 'Cartagena',["741852963", "85214567", "741852444"])
            _controllerFlight.create_flight('LATAM', 'tango-03', 'LA100', data, 'Medellín', 'Bogota', ["963258741", "741852963"])
            _controllerFlight.create_flight('JetBlue', 'tango-04', 'JB200', data, 'Bogota', 'Medellín', ["963258741", "741852963"])
