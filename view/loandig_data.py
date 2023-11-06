from model.person import Person
from controller.aircraft_controller import AircraftController

controllerAircraft = AircraftController()

def loandig_data_default() -> None:

    #### Aircraft ####

    controllerAircraft.create_aircraft( "plane", "tango-00", "mitsubishi", "airbus", "100A.C", 10, 20, 10000, heightMax = 840, nEngines = 2, category = "comercial" );

    controllerAircraft.create_aircraft( "helicopter", "tango-01", "mitsubishi", "airbus", "100A.C", 10, 20, 10000, heightMax = 840, nRotors = 1, liftingCapacity = 200, specificUse = "rescate" )

    controllerAircraft.create_aircraft( "jet", "tango-02", "mitsubishi", "airbus", "100A.C", 10, 20, 10000, cedula = "1110101", name = "oscar" , surname = "vargas", birthDate = 'today', genre = "macho", address = "en tu casa", phoneNumber = "0135462013", email = "hola@gmail.com")

    

