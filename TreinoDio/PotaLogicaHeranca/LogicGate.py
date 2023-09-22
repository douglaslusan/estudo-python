class LogicGate:

    def __init__(self, n):
        self.name = n
        self.output = None

    def get_name(self):
        return self.name

    def get_output(self):
        self.output = self.perform_gate_logic()
        return self.output
