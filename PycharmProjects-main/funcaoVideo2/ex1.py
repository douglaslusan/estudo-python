def voto(ano):
	from datetime import datetime
	atual = datetime.today().year
	idade = atual - ano
	if idade < 16:
		return f'idade {idade} => nao vota'
	elif idade < 18 or idade > 65:
		return f'idade {idade} => voto opcional'
	else:
		return f'idade {idade} => voto é obrigatorio'


ano = int(input('em que ano vc nasceu: '))
print(voto(ano))

