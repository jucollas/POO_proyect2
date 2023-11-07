from model.person import Person
from controller.aircraft_controller import AircraftController
from controller.airline_controller import AirlineController
from controller.controlTower_controller import ControlTower_controller
from controller.boardingGate_controller import BoardingGate_Controller
from controller.crew_controller import CrewController
from controller.flight_controller import FlightController

import datetime

controllerAircraft = AircraftController()
controllerAirline = AirlineController()
controllerCT = ControlTower_controller()
controllerBC = BoardingGate_Controller()
controllerCrew = CrewController()
controlerFlight = FlightController()

def loandig_data_default() -> None:

    #### Aircraft ####

    controllerAircraft.create_aircraft( "plane", "tango-00", "mitsubishi", "airbus", "100A.C", 10, 20, 10000, heightMax = 840, nEngines = 2, category = "comercial" );

    controllerAircraft.create_aircraft( "helicopter", "tango-01", "mitsubishi", "airbus", "100A.C", 10, 20, 10000, heightMax = 840, nRotors = 1, liftingCapacity = 200, specificUse = "rescate" )

    controllerAircraft.create_aircraft( "jet", "tango-02", "mitsubishi", "airbus", "100A.C", 10, 20, 10000, cedula = "1110101", name = "oscar" , surname = "vargas", birthDate = 'today', genre = "macho", address = "en tu casa", phoneNumber = "0135462013", email = "hola@gmail.com")

    controllerAirline.create_airline('Avianca')
    controllerAirline.create_airline('Viva')

    controllerCT.create_airport('Cali')
    controllerCT.create_airport('Bogota')
    controllerCT.create_airport('Cartagena')

    controllerBC.create_boardingGate('Cali', 'A0', 'Norte')
    controllerBC.create_boardingGate('Cali', 'A1', 'Norte')
    controllerBC.create_boardingGate('Cali', 'A2', 'Norte')
    controllerBC.create_boardingGate('Bogota', 'A0', 'Sur')
    controllerBC.create_boardingGate('Bogota', 'A1', 'Norte')
    controllerBC.create_boardingGate('Bogota', 'A2', 'Oeste')
    controllerBC.create_boardingGate('Cartagena', 'A0', 'Norte')
    controllerBC.create_boardingGate('Cartagena', 'A1', 'Norte')
    controllerBC.create_boardingGate('Cartagena', 'A2', 'Norte')

    data = datetime.date(2023,11,6)

    controllerCrew.create_crewMember("741852963", "Sara", "Salazar", data, 'Femenino', 'Cr 12 N 8-22', '32314154', 'sara@gmail.com', 'Piloto', 10, 20 )
    controllerCrew.create_crewMember("85214567", "Santiago", "Salazar", data, 'Masculino', 'Cr 12 N 8-22', '32314154', 'sara@gmail.com', 'Piloto', 10, 20 )
    controllerCrew.create_crewMember("741852444", "Camila", "Salazar", data, 'Femenino', 'Cr 12 N 8-22', '32314154', 'sara@gmail.com', 'Piloto', 10, 20 )



    controlerFlight.create_flight('Viva', 'tango-00', 'AV000', data, 'Cali', 'Bogota',["741852963", "85214567", "741852444"])
    controlerFlight.create_flight('Avianca', 'tango-00', 'AV001', data, 'Bogota', 'Cali',["741852963", "85214567", "741852444"])
    controlerFlight.create_flight('Viva', 'tango-01', 'AV002', data, 'Cali', 'Cartagena',["741852963", "85214567", "741852444"])
    controlerFlight.create_flight('Avianca', 'tango-02', 'AV003', data, 'Bogota', 'Cartagena',["741852963", "85214567", "741852444"])
