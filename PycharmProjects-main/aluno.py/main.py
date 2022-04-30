class Conta:
    def __init__(self, nome, numero):
        self.cliente = nome
        self.num = numero
        self.saldo = 0.0

    def Saldo(self):
        return self.saldo

    def GetCliente(self):
        return self.cliente

    def Depositar(self, valor):
        self.saldo += valor

    def Sacar(self, valor):
        self.saldo -= valor
