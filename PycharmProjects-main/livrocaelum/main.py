class Conta:
    def __init__(self, numero, titular, saldo, limite):
        self.numero = numero
        self.titular = titular.title()
        self._saldo = saldo
        self.limite = limite


    def deposita(self, valor):
        self._saldo += valor
        print(f'depositado o valor de {valor}\n')
            


    def saca(self, valor):
        if(valor < self._saldo):
            self._saldo -= valor
            print(f'sacado o valor de {valor}\n')

        if(valor > self._saldo):
            self._saldo -= valor
            self.limite += self._saldo
            print(f'sacado o valor de {valor}\n')

        if(valor > self._saldo + self.limite):
            print(f'O valor de saque é indisponivel \n')

    def extrato(self):
        print(f'O saldo da conta do titular {self.titular} é de {self._saldo} e seu limite de {self.limite}\n')


conta = Conta(1, 'douglas', 100, 1000)

conta.extrato()

conta.deposita(200)

conta.extrato()

conta.saca(500)

conta.extrato()