def cria_matriz(n_linha, n_coluna):
	matriz = []
	for i in range(n_linha):
		linha = []
		for j in range(n_coluna):
			valor = int(input(f'digite o valor da posicao [{i}][{j}]: '))
			linha.append(valor)

		matriz.append(linha)
	return matriz

def ler_matriz():
	linha = int(input('digite a quantia de linhas: '))
	coluna = int(input('digite a quantia de colunas: '))
	return cria_matriz(linha, coluna)


mat = ler_matriz()
print(mat)