
import ATM as atm


print("*******BEM VINDO AO BANCO DOUGLAS*******")
print("___________________________________________________________\n")
print("----------CRIACAO DE CONTA----------")
name = input("ENTRE COM SEU NOME: ")
account_number = input("ENTRE COM O NUMERO DA SUA CONTA: ")
print("PARABENS. SUA CONTA FOI CRIADA COM SUCESSO......\n")

atm = atm.ATM(name, account_number)

while True:
    trans = input("QUER REALIZAR ALGUMA TRANSACAO?(s/n): ").lower()
    if trans == "s":
        atm.transaction()
    elif trans == "n":
        print("""
    -------------------------------------
   | obrigado por escolher nosso banco |
   | Visite nos novamente!                     |
    -------------------------------------
        """)
        break
    else:
        print("comando errado!  Entre 's' para sim e 'n' para nao.\n")
