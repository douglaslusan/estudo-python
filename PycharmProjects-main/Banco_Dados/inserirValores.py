import sqlite3

banco = sqlite3.connect('primeiro_banco.db')

cursor = banco.cursor()

def inserirValores():
	try:
		nome = input('digite o nome da pessoa: ')
		idade = int(input('digite a idade: '))
		cpf = input('digite o CPF: ')
		email = input('digite o email da pessoa: ')
		telefone = input('digite o telefone: ')

		cursor.execute("""INSERT INTO Pessoas(nome, idade, cpf, email, fone)
					   VALUES(?,?,?,?,?)""", (nome, idade, cpf, email, telefone))

		banco.commit()

		banco.close()

	except sqlite3.Error as erro:
		print('Erro ao inserir dados na tabela', erro)
