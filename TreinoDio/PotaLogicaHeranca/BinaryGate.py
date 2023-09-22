from LogicGate import LogicGate


class BinaryGate(LogicGate):

    def __init__(self, n):
        LogicGate.__init__(self, n)

        self.pinA = None
        self.pinB = None

    def get_pin_a(self):
        if self.pinA is None:
            return int(input("Enter Pin A input for gate " + self.get_name() + "-->"))
        else:
            return self.pinA.get_from().get_output()

    def get_pin_b(self):
        if self.pinB is None:
            return int(input("Enter Pin B input for gate " + self.get_name() + "-->"))
        else:
            return self.pinB.get_from().get_output()

    def set_next_pin(self, source):
        if self.pinA is None:
            self.pinA = source
        else:
            if self.pinB is None:
                self.pinB = source
            else:
                print("Cannot Connect: NO EMPTY PINS on this gate")
