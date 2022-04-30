aluno = dict()

aluno['nome'] = str(input('nome: '))
aluno['media'] = float(input('Media: '))

if aluno['media'] >= 7.0:
	aluno['situacao'] = 'aprovado'
elif aluno['media'] >= 5.0:
	aluno['situacao'] = 'recuperacao'
else:
	aluno['situacao'] = 'reprovado'

print(f'Nome: {aluno["nome"]}')
print(f'Sua media: {aluno["media"]}')
print(f'Sua situacao é {aluno["situacao"]}')