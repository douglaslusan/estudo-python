# 1 Exception
# 	Classe base para todas as exceções
#
# 2 StopIteration
# 	Gerado quando o método next() de um iterador não aponta para nenhum objeto
#
# 3 SystemExit
# 	Gerado pela função sys.exit().
#
# 4 StandardError
# 	Classe base para todas as exceções internas, exceto StopIteration e SystemExit.
#
# 5 ArithmeticError
# 	Classe base para todos os erros que ocorrem no cálculo numérico.
#
# 6 OverflowError
# 	Gerado quando um cálculo excede o limite máximo para um tipo numérico.
#
# 7 FloatingPointError
# 	Gerado quando um cálculo de ponto flutuante falha.
#
# 8 ZeroDivisionError
# 	Gerado quando a divisão ou módulo por zero ocorre para todos os tipos numéricos.
#
# 9 AssertionError
# 	Gerado em caso de falha da declaração Assert.
#
# 10 AttributeError
# 	Gerado em caso de falha de referência ou atribuição de atributo.
#
# 11 EOFError
# 	Gerado quando não há entrada da função raw_input() ou input() e o final do arquivo é atingido.
#
# 12 ImportError
# 	Gerado quando uma instrução de importação falha.
#
# 13 KeyboardInterrupt
# 	Gerado quando o usuário interrompe a execução do programa, geralmente pressionando Ctrl+c.
#
# 14 LookupError
# 	Classe base para todos os erros de pesquisa.
#
# 15 IndexError
# 	Gerado quando um índice não é encontrado em uma sequência.
#
# 16 KeyError
# 	Gerado quando a chave especificada não é encontrada no dicionário.
#
# 17 NameError
# 	Gerado quando um identificador não é encontrado no namespace local ou global.
#
# 18 UnboundLocalError
# 	Gerado ao tentar acessar uma variável local em uma função ou método,
# 	mas nenhum valor foi atribuído a ela.
#
# 19 EnvironmentError
# 	Classe base para todas as exceções que ocorrem fora do ambiente Python.
#
# 20 IOError
# 	Gerado quando uma operação de entrada/saída falha,
# 	como a instrução print ou a função open() ao tentar abrir um arquivo que não existe.
#
# 21 IOError
# 	Gerado para erros relacionados ao sistema operacional.
#
# 22	SyntaxError
# 	Gerado quando há um erro na sintaxe do Python.
#
# 23	IndentationError
# 	Gerado quando o recuo não é especificado corretamente.
#
# 24	SystemError
# 	Gerado quando o interpretador encontra um problema interno, mas quando esse erro é encontrado,
# 	o interpretador Python não sai.
#
# 25	SystemExit
# 	Gerado quando o interpretador Python é encerrado usando a função sys.exit().
# 	Se não for tratado no código, faz com que o interpretador saia.
#
# 26	TypeError
# 	Gerado quando uma operação ou função é tentada que é inválida para o tipo de dados especificado.
#
# 27	ValueError
# 	Gerado quando a função interna de um tipo de dados tem o tipo válido de argumentos,
# 	mas os argumentos têm valores inválidos especificados.
#
# 28	RuntimeError
# 	Gerado quando um erro gerado não se enquadra em nenhuma categoria.
#
# 29 NotImplementedError
# 	Gerado quando um método abstrato que precisa ser implementado
# 	em uma classe herdada não é realmente implementado.

'''def KelvinToFahrenheit(Temperature):
	assert (Temperature >= 0), "Colder than absolute zero!"
	return ((Temperature - 273) * 1.8) + 32


print(KelvinToFahrenheit(273))
print(int(KelvinToFahrenheit(505.78)))
print(KelvinToFahrenheit(-5))'''

# try:
# 	fh = open("testfile.txt", "w")
# 	fh.write("This is my test file for exception handling!!")
# except IOError:
# 	print("Error: can\'t find file or read data")
# else:
# 	print("Written content in the file successfully")
# 	fh.close()


# try:
# 	fh = open("testfile.txt", "r")
# 	fh.write("This is my test file for exception handling!!")
# except IOError:
# 	print("Erro: este arquivo nao pode ser gravado")
# else:
# 	print("escrito no arquivo com sucesso")

# try:
# 	fh = open("testfile", "w")
# 	try:
# 		fh.write("This is my test file for exception handling!!")
# 	finally:
# 		print("Going to close the file")
# 		fh.close()
# except IOError:
# 	print("Error: can\'t find file or read data")

# def temp_convert(var):
# 	try:
# 		return int(var)
# 	except ValueError as Argument:
# 		print("The argument does not contain numbers\n", Argument)
#
# # Call above function here.
# print(temp_convert("xyz"))

# class Networkerror(RuntimeError):
# 	def __init__(self, arg):
# 		self.args = arg
#
#
# try:
# 	raise Networkerror("Bad hostname")
# except Networkerror as e:
# 	print(e.args)

