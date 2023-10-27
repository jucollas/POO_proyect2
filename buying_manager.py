from flight import Flight
from passenger import Passenger

class BuyingManager:
    def __init__(self):
        self.scheduled_flights: dict[str, Flight] = {}

    def schedule_flight(self, flight_id: str, passenger: Passenger) -> bool:
        res = False
        if flight_id not in self.scheduled_flights:
            print(f"Error: the flight code '{flight_id}' isn't valid.")
        elif self.scheduled_flights[flight_id].has_available_seats():
            res = self.scheduled_flights[flight_id].book_seat(passenger)
        else:
            print("Error: not enough space in the aircraft.")
        return res

    def filter_and_print_flight(self, date : str = None, origin : str = None, destiny: str = None) -> list[str]:
        res = []
        for flight_id, flight in self.scheduled_flights.items():
            if (date is None or date == flight.get_date()) and (origin is None or origin == flight.get_origin()) and (destiny is None or destiny == flight.get_destiny()):
                booked_seats = flight.get_booked_seats()
                ability_pass = flight.get_aircraft().get_ability_pass()
                print(f"[{len(res)}] {flight.get_flight_code()} | date: {flight.get_date()}, origin: {flight.get_origin()}, destiny: {flight.get_destiny()}. With [{booked_seats}/{ability_pass}] available seats.")
                res.append(flight_id)
        return res

    def add_flight(self, flight: Flight) -> None:
        self.scheduled_flights[flight.get_flight_code()] = flight

    def del_flight(self, flight_id: str) -> None:
        if flight_id in self.scheduled_flights:
            del self.scheduled_flights[flight_id]

    def info(self) -> None:
        print(f"There are {len(self.scheduled_flights)} scheduled flights.")
        for flight in self.scheduled_flights.values():
            flight.info()
