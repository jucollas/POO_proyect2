from boarding_gate import BoardingGate
from flight import Flight

class GateControl:
    def __init__(self):
        self._gates : dict[str, BoardingGate] = {}

    def bookBoardingGate(self, flight):
        for gate_id, gate in self._gates.items():
            if gate.isAvailable():
                if gate.assignFlight(flight):
                    return gate_id
        print("Error: impossible to book a gate")
        return None

    def freeBoardingGate(self, gate_id):
        if gate_id in self._gates:
            gate = self._gates[gate_id]
            if gate.isAvailable():
                print(f"The gate '{gate_id}' is already free.")
            else:
                gate.dispatchFlight()
                print(f"The gate '{gate_id}' is now free.")
        else:
            print(f"Error: the gateId '{gate_id}' is not in the gates")

    def addGate(self, id, location):
        gate = BoardingGate(id, location)
        self._gates[id] = gate

    def info(self):
        print(f"There are {len(self._gates)} gates:")
        for gate in self._gates.values():
            gate.info()

    def __del__(self):
        for gate in self._gates.values():
            del gate
