from datetime import datetime

funcionario = dict()

funcionario['nome'] = input('digite o nome: ')
nasc = int(input('ano de nascimento: '))
funcionario['ctps'] = int(input('digite a CTPS: [0] Não tem carteira'))
contratacao = int(input('ano de contratação: '))
salario = float(input('digite o salario: '))

funcionario['idade'] = datetime.now().year - nasc
if funcionario['ctps'] != 0:
	funcionario['Ano_contratacao'] = contratacao
	funcionario['salario'] = salario
	aposentadoria = contratacao + 35
	funcionario['aposentadoria'] = aposentadoria - nasc
else:
	print('nao possui carteira assinada')
print('-='*30)
for k, v in funcionario.items():
	print(f'{k}: {v}')