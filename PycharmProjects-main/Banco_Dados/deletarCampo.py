import sqlite3

banco = sqlite3.connect('Primeiro_banco.db')

cursor = banco.cursor()

def deletarRegistroPorNome():
	try:
		id_Pessoa = int(input('digite o ID a ser deletado: '))

		cursor.execute("""DELETE FROM Pessoas WHERE id = ?""", (id_Pessoa,))

		banco.commit()

		print('Campo apagado')

	except sqlite3.Error as erro:
		print('erro ao apagar Campo', erro)
