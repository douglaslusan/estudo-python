def busca_binaria(lista, elemento):
	minimo = 0
	maximo = len(lista) - 1
	encontrado = False

	while minimo <= maximo and not encontrado:
		meio_lista = (minimo + maximo) // 2
		if lista[meio_lista] == elemento:
			encontrado = True
		else:
			if elemento < lista[meio_lista]:
				maximo = meio_lista - 1
			else:
				minimo = meio_lista + 1

	return encontrado


set1 = set('douglas luiz dos santos')
print(type(set1))
print(set1)

lista = [2,4,8,3,0,4,7,9,1]

if busca_binaria(lista, 4):
	print('encontrado')
else:
	print('nao encontrado')


