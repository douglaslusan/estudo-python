import random
import sys

class ATM:
    def __init__(self, name, account_number, balance=0):
        self.name = name
        self.account_number = account_number
        self.balance = balance

    def account_detail(self):
        print("\n----------DETALHE DA CONTA----------")
        print(f"CLIENTE: {self.name.upper()}")
        print(f"NUMERO DA CONTA: {self.account_number}")
        print(f"SALDO AVALIADO.{self.balance}\n")

    def deposit(self, amount):
        self.amount = amount
        self.balance = self.balance + self.amount
        print("SALDO.", self.balance)
        print()

    def withdraw(self, amount):
        self.amount = amount
        if self.amount > self.balance:
            print("SALDO INSUFICIENTE!")
            print(f"SEU SALDO {self.balance}.")
            print("TENTE UM VALOR MENOR.")
            print()
        else:
            self.balance = self.balance - self.amount
            print(f"${amount} SAQUE COM SUCESSO!")
            print("SALDO", self.balance)
            print()

    def check_balance(self):
        print("SALDO", self.balance)
        print()

    def transaction(self):
        print("""
            Transação 
        *********************
            Menu:
            1. Detalhe da conta
            2. Checar saldo
            3. Depositar
            4. Sacar
            5. Sair
        *********************
        """)

        while True:
            try:
                option = int(input("Entre 1, 2, 3, 4 or 5: "))
            except:
                print("Erro: Entre 1, 2, 3, 4, or 5 somente!\n")
                continue
            else:
                if option == 1:
                    self.account_detail()
                elif option == 2:
                    self.check_balance()
                elif option == 3:
                    amount = int(input("Valor a ser depositado: "))
                    self.deposit(amount)
                elif option == 4:
                    amount = int(input("Valor a ser sacado: "))
                    self.withdraw(amount)
                elif option == 5:
                    print(f"""
                Imprimindo Extrato..............
          ******************************************
              Transação completa.                         
              Transação numero: {random.randint(10000, 1000000)} 
              Cliente: {self.name.upper()}                  
              Numero da conta: {self.account_number}                
              Saldo avaliado: ${self.balance}                    

              obrigado por escolher nosso banco                  
          ******************************************
          """)
                    sys.exit()