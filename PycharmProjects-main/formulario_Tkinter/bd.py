import sqlite3

# criando conexao

conexao = sqlite3.connect("dados.bd")

# criando tabela

with conexao:
	cursor = conexao.cursor()
	cursor.execute("CREATE TABLE formulario(id INTEGER PRIMARY KEY AUTOINCREMENT,"
				" nome TEXT, email TEXT, telefone TEXT, Nascimento DATE, estado TEXT, assunto TEXT)")

