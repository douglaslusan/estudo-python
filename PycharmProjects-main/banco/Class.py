class Conta:
    def __init__(self, nome, numero):
        self.__cliente = nome
        self.num = numero
        self.__saldo = 0.0


    def GetSaldo(self):
        return self.__saldo

    def GetCliente(self):
        return self.__cliente

    def Depositar(self, valor):
        self.__saldo += valor

    def Sacar(self, valor):
        self.__saldo -= valor

    def Transferencia(self, conta, valor):
        self.__saldo -= valor
        conta.__saldo += valor
