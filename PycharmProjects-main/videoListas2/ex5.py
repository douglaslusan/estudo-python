from random import randint

sena = []
jogos = list()
total = 0
opc = int(input('digite quantos jogos vc quer realizar '))

while total < opc:
	cont = 0
	while(True):
		n = randint(1, 60)
		if n not in sena:
			sena.append(n)
			cont += 1
		if cont >= 6:
			break

	sena.sort()
	jogos.append(sena[:])
	sena.clear()
	total += 1
print()
print("-=" * 11,	f'FORAM SORTEADOS {opc} JOGOS',	"-=" * 11)
print()
for i, j in enumerate(jogos):
	print(f' jogo {i+1}: {j}')
print()
print('*'*30,  'BOA SORTE', '*'*30)