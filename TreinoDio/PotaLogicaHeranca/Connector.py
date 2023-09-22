class Connector:

    def __init__(self, fgate, tgate):
        self.fromgate = fgate
        self.togate = tgate

        tgate.set_next_pin(self)

    def get_from(self):
        return self.fromgate

    def get_to(self):
        return self.togate
