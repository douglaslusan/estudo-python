def escreva(txt):
	t = len(txt) + 4
	print(f'{"-"*t}')
	print(f'{txt:^{t}}')
	print(f'{"-"*t}')


escreva('Douglas Luiz dos Santos')
