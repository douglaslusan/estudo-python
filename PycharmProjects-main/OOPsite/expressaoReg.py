import re

line = 'Gatos sao menores que caes'

matchObj = re.match(r'(.*) sao (.*?) .*', line, re.M | re.I)

if matchObj:
	print('MatchObj.group(): ', matchObj.group())
	print('MatchObj.group(1): ', matchObj.group(1))
	print('MatchObj.group(2): ', matchObj.group(2))
else:
	print('no Match')

searchObj = re.search(r'sao', line)

if searchObj:
	print('searchObj.group: ', searchObj.group())
else:
	print('nao encontrado')


fone = '99758-1602 # este é um numero de telefone'

num = re.sub(r'#.*$', '', fone)	 # remove caracteres apos o '#'
print(num)

num = re.sub(r'\D', '', fone)	 # remove caracteres que nao sao numeros
print(num)

