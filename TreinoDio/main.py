# 1º desafio Python DIO
# saldo_atual = 100
# valor_deposito = 10
# valor_retirada = 50
#
# # TODO: Calcular o saldo atualizado de acordo com a descrição deste desafio.
# class Bank:
# 	def __init__(self, saldo_atual):
# 		self.saldo = saldo_atual
#
# 	def Saldo(self):
# 		print(self.saldo)
#
# 	def Deposito(self, valor_deposito):
# 		self.saldo += valor_deposito
#
# 	def Retirada(self, valor_retirada):
# 		self.saldo -= valor_retirada
#
#
# # TODO: Imprimir o a saída de conforme a tabela de exemplos (uma casa decimal).
#
# cliente = Bank(saldo_atual)
# cliente.Deposito(valor_deposito)
# cliente.Retirada(valor_retirada)
# print(cliente.saldo)

# 2 Desafio Python DIO
#
# ativos = []
#
# # Entrada da quantidade de ativos
# quantidadeAtivos = int(input())
#
# # Entrada dos códigos dos ativos
# for i in range(quantidadeAtivos):
# 	codigoAtivo = input()
# 	ativos.append(codigoAtivo)
#
# # TODO: Ordenar os ativos em ordem alfabética.
# ativos.sort()
#
# # TODO: Imprimir a lista de ativos ordenada, conforme a tabela de exemplos.
# for i in ativos:
# 	print(i)

# 3 Desafio Python DIO

# Entrada de dados
# saldo_total = int(input())
# valor_saque = int(input())
#
# TODO: Criar as condições necessárias para impressão da saída, vide tabela de exemplos.
# class Bank:
# 	def __init__(self, saldo_total):
# 		self.saldo = saldo_total
#
# 	def Retirada(self, valor_saque):
# 		if self.saldo < valor_saque:
# 			print("Saldo insuficiente. Saque nao realizado!")
# 		else:
# 			self.saldo -= valor_saque
# 			print(f"Saque realizado com sucesso! Novo saldo: {self.saldo}")
#
#
# cliente = Bank(saldo_total)
#
# cliente.Retirada(valor_saque)

# 4 Desafio Python DIO

# valor_inicial = 5000
# taxa_juros = 0.08
# periodo = 5
#
# def calcular_valor_futuro(valor_inicial, taxa_juros, periodo):
#     valor_futuro = valor_inicial * (1 + taxa_juros) ** periodo
#     return valor_futuro
#
# valor_final = calcular_valor_futuro(valor_inicial, taxa_juros, periodo)
#
# # TODO: Iterar, baseado no período em anos, para calculo do valorFinal com os juros.
#
#
# print(f"Valor final do investimento: R$ {valor_final:.2f}")

# 5 Desafio Python DIO

# valor = float(input())
#
#
# class Bank:
# 	def __init__(self, saldo_atual):
# 		self.saldo = saldo_atual
#
#
# 	def Deposito(self, valor_deposito):
# 		# TODO: Imprimir a mensagem de sucesso, formatando o saldo atual (vide Exemplos).
# 		if valor > 0:
# 			self.saldo += valor_deposito
# 			print(f'Deposito realizado com sucesso! Saldo atual: R$ {self.saldo:.2f}')
# 		# TODO: Imprimir a mensagem de valor inválido.
# 		elif valor == 0:
# 			print(f'Encerrando o programa...')
# 			return
# 		# TODO: Imprimir a mensagem de encerrar o programa.
# 		else:
# 			print(f'Valor invalido! Digite um valor maior que zero.')
#
# 	def Retirada(self, valor_retirada):
# 		self.saldo -= valor_retirada
#
# cliente = Bank(500)
#
# cliente.Deposito(valor)

