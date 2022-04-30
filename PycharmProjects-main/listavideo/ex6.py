expres = str(input('digite a expressao: '))
pilha = []

for simb in expres:
	if simb == '(':
		pilha.append('(')
	elif simb == ')':
		if len(pilha) > 0:
			pilha.pop()
		else:
			pilha.append(')')
			break
print(pilha)
if len(pilha) == 0:
	print('sua expressao está válida')
else:
	print('sua expressao não está válida')
