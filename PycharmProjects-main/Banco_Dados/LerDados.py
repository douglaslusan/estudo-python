import sqlite3

banco = sqlite3.connect('primeiro_banco.db')
cursor = banco.cursor()

sql = 'SELECT * FROM Pessoas WHERE nome = ?'

def ler_dado():
	palavra = input('digite o nome que deseja: ')
	for row in cursor.execute(sql, (palavra,)):
		# print(row[2])
		print(row)

