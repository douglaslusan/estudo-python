lista = list()
n = 0
for i in range(0, 5):
	print(lista)
	n = int(input('digite um valor: '))
	if i == 0 or n > lista[-1]:
		lista.append(n)
	else:
		pos = 0

		while pos < len(lista):
			if n <= lista[pos]:
				lista.insert(pos, n)
				break
			pos += 1

print(f'Sua lista {lista}')