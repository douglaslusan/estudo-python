from CriarTabela import *
from deletarCampo import *
from inserirValores import *
from LerDados import *

while(True):
	opc = int(input('Digite 1 para criar tabela\n'
					'Digite 2 para inserir dados\n'
					'Digite 3 para deletar Registro\n'
					'Digite 4 para ler nome\n'
					'Digite 0 para sair '))

	if opc == 0:
		banco.close()
		break

	if opc == 1:
		createTab()

	if opc == 2:
		inserirValores()

	if opc == 3:
		deletarRegistroPorNome()

	if opc == 4:
		ler_dado()

	print('\n')

