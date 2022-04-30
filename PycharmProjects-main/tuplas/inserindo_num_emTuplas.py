numero = (int(input("digite um numero: ")),
          int(input("digite um numero: ")),
          int(input("digite um numero: ")),
          int(input("digite um numero: ")))

print(numero)

print(f'apareceu o numero 9 => {numero.count(9)}x ')

if 3 in numero:
    print(f'apareceu o numero 3 pela primeira vez => na posicao {numero.index(3)} ')
else:
    print('o numero 3 nao apareceu em nenhuma posicao')

print('o numero par digitado foi ')
for n in numero:
    if n % 2 == 0:
        print(n, end=', ')


