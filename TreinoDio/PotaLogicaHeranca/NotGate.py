from UnaryGate import *


class NotGate(UnaryGate):

    def __init__(self, n):
        UnaryGate.__init__(self, n)

    def perform_gate_logic(self):
        if self.get_pin():
            return 0
        else:
            return 1
