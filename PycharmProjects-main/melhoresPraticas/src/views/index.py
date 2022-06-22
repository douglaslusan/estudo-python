import sys
from pathlib import Path
file = Path(__file__).resolve()
parent, root = file.parent, file.parents[1]
sys.path.append(str(root))

from controler.pessoa import Pessoa, PessoaController
from models.pessoa import Pessoa

while True:
	decisao = int(input('digite 1 para salvar e 2 para listar '))

	if decisao == 1:
		nome = input('Nome: ')
		sobrenome = input('Sobrenome: ')
		idade = input('idade: ')
		cpf = input('CPF: ')

		p1 = Pessoa(nome=nome, sobrenome=sobrenome, idade=idade, cpf=cpf)
		PessoaController.salvarPessoa(p1)

	elif decisao == 2:
		for i in PessoaController.listarPessoas():
			print(f'Nome: {i.nome}')
			print(f'sobrenome: {i.sobrenome}')
			print(f'idade: {i.idade}')
			print(f'CPF: {i.cpf}')
			print()