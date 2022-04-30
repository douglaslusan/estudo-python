lista = list()
pares = list()
impares = list()

while True:
	n = int(input('Digite um numero positivo ou negativo para sair: '))
	if n > 0:
		lista.append(n)
	else:
		break
for p in lista:
	if p % 2 == 0:
		pares.append(p)
	else:
		impares.append(p)

print(f'Lista {lista}')
print(f'lista de pares {pares}')
print(f'lista de impares {impares}')