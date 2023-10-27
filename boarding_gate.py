from flight import Flight

class BoardingGate:
    def __init__(self, identification: str, location: str) -> None:
        self.identification = identification
        self.location = location
        self.inGate = None
        self.boardingTime = ""
        self.history = []

    def get_identification(self) -> str:
        return self.identification

    def get_location(self) -> str:
        return self.location

    def get_history(self) -> list[Flight]:
        return self.history

    def get_in_gate(self) -> Flight:
        return self.inGate

    def assign_flight(self, f: Flight) -> bool:
        res = self.is_available()
        if res:
            self.inGate = f
            self.boardingTime = f.get_date()
        return res

    def dispatch_flight(self) -> None:
        if self.inGate is not None:
            self.history.append(self.inGate)
            self.inGate = None

    def is_available(self) -> bool:
        return self.inGate is None

    def info(self) -> None:
        info_str = f"Gate: {self.identification}, located in {self.location}."
        if self.inGate is None:
            info_str += " It hosts no flight."
        else:
            info_str += f" It hosts flight with code: {self.inGate.get_flight_code()} at {self.boardingTime}."
        print(info_str)
