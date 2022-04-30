import sqlite3


def createTab():
	try:
		banco = sqlite3.connect('primeiro_banco.db')

		cursor = banco.cursor()

		cursor.execute(
			"CREATE TABLE IF NOT EXISTS Pessoas(id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,"
			" nome TEXT NOT NULL, idade INTEGER, cpf VARCHAR(11) NOT NULL, email TEXT NOT NULL,"
			" fone TEXT)")

		banco.commit()
		banco.close()

	except sqlite3.Error as erro:
		print('Erro ao criar tabela', erro)
