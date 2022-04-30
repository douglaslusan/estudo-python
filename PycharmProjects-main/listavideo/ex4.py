lista = list()

while True:
	n = int(input('Digite um numero positivo ou negativo para sair: '))
	if n > 0:
		lista.append(n)

	else:
		break

if 5 in lista:
	print('5 esta incluso na lista')
else:
	print('nao contem o valor 5 na lista')

lista.sort(reverse=True)
print(f'sua lista contem {len(lista)} valores\n{lista}')