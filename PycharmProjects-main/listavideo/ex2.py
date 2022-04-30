lista = list()
n = 0
while(n >= 0):
	n = int(input('digite um numero positivo ou negativo para sair: '))
	if(n not in lista and n > 0):
		lista.append(n)


print(sorted(lista))
