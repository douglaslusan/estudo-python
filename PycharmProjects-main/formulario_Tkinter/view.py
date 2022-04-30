import sqlite3

con = sqlite3.connect("dados.bd")


# Inserindo informacoes
def mostrar_info():
	lista = []
	with con:
		cursor = con.cursor()
		query = "SELECT * FROM Formulario"
		cursor.execute(query)
		info = cursor.fetchall()

		for i in info:
			lista.append(i)
	return lista

def inserir_info(i):
	with con:
		cursor = con.cursor()
		query = "INSERT INTO Formulario(nome, email, telefone, Nascimento, estado, assunto) VALUES(?,?,?,?,?,?)"
		cursor.execute(query, i)


# atualizar informacoes
def atualizar_info(i):
	with con:
		cursor = con.cursor()
		query = "UPDATE formulario SET nome=?, email=?, telefone=?, Nascimento=?, estado=?, assunto=? WHERE id=?"
		cursor.execute(query, i)



# DELETAR informacoes
def deletar_info(i):
	with con:
		cursor = con.cursor()
		query = "DELETE FROM formulario WHERE id=?"
		cursor.execute(query, i)
