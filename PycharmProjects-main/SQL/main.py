import sqlite3

conector = sqlite3.connect("Conta.db")
cursor = conector.cursor()

sql = """create table cadastro(codigo integer, nome text, idade integer)"""


sql = """insert into cadastro(codigo, nome, idade) values(2308, 'douglas luiz', 42)"""
cursor.execute(sql)
sql = """insert into cadastro(codigo, nome, idade) values(0709, 'Raziel', 6)"""

cursor.execute(sql)



conector.commit()
cursor.close()
conector.close()
