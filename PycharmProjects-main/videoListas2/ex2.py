numeros = [[], []]
n = 0
for i in range(0, 7):
	n = int(input('digite um numero: '))
	if n % 2 == 0:
		numeros[0].append(n)
	else:
		numeros[1].append(n)

print(f'os valores pares em ordem {sorted(numeros[0])}')
print(f'os valores impares em ordem {sorted(numeros[1])}')