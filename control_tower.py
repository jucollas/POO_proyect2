from flight import Flight
from message import Message
from gate_control import GateControl

class ControlTower:
    def __init__(self):
        self.instance = None
        self.flights : set[Flight] = set()
        self.gateControl = GateControl()

    @staticmethod
    def get_instance() -> 'ControlTower':
        if ControlTower.instance is None:
            ControlTower.instance = ControlTower()
        return ControlTower.instance

    def add_flight(self, f: Flight) -> None:
        self.flights.add(f)

    def delete_flight(self, f: Flight) -> None:
        self.flights.discard(f)

    def notify_flights(self, m: Message) -> None:
        for f in self.flights:
            f.receive_message(m)

    def book_boarding_gate(self, f: Flight) -> str:
        return self.gateControl.book_boarding_gate(f)

    def free_boarding_gate(self, gate_id: str) -> None:
        self.gateControl.free_boarding_gate(gate_id)

    def info(self) -> None:
        print(f"There are {len(self.flights)} flights connected to the control tower.")
        for f in self.flights:
            f.info()
        self.gateControl.info()

    def add_gate(self, id: str, location: str) -> None:
        self.gateControl.add_gate(id, location)
