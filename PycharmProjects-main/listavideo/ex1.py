listaA = list()
maior = menor = 0
for i in range(0,5):
	listaA.append(int(input(f'digite um numero na posicao {i}: ')))
	if i == 0:
		maior = menor = listaA[i]
	else:
		if listaA[i] > maior:
			maior = listaA[i]
		if listaA[i] < menor:
			menor = listaA[i]

print(listaA)
for c, i in enumerate(listaA):
	if (i == menor):
		print(f'o menor {menor} esta na posicao {c}')

for c, i in enumerate(listaA):
	if (i == maior):
		print(f'o maior {maior} esta na posicao {c}')