from model.airport import Airport

class Airport_Controller:

    def __init__(self) -> None:
        self._airport : Airport = Airport()
        
    def create_crew(self, cedula : str, name : str, surname : str, birthDate : str, genre : str, address : str, phoneNumber : str, email : str, jobPosition : str,  dailyWorkingHours : int, yearsExperience : int) -> None:
        self._airport.create_crew(cedula, name, surname, birthDate, genre, address, phoneNumber, email, jobPosition, dailyWorkingHours, yearsExperience)

        
