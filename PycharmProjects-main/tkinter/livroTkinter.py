from tkinter import *


# class Janela:
# 	def __init__(self, toplevel):
# 		self.fr1 = Frame(toplevel)
# 		self.fr1['bg'] = 'yellow'
# 		self.fr1.pack()
# 		self.botao1 = Button(self.fr1, text='Oi!')
# 		self.botao1['bg'] = 'cyan'
# 		self.botao1['font'] = ('verdana', '20', 'italic', 'bold')
# 		self.botao1['width'] = 20
# 		self.botao1.pack()
# 		self.botao2 = Button(self.fr1, bg='blue', font=('verdana', '20'))
# 		self.botao2['text'] = 'Tchau!'
# 		self.botao2['fg'] = 'cyan'
# 		self.botao2['width'] = 20
# 		self.botao2.pack(side=BOTTOM)

# class Packing:
# 	def __init__(self, instancia_Tk):
# 		self.container1 = Frame(instancia_Tk)
# 		self.container2 = Frame(instancia_Tk)
# 		self.container3 = Frame(instancia_Tk)
# 		self.container1.pack()
# 		self.container2.pack()
# 		self.container3.pack()
# 		Button(self.container1, text='B1').pack()
# 		Button(self.container2, text='B2').pack(side=LEFT)
# 		Button(self.container2, text='B3').pack(side=LEFT)
# 		self.b4 = Button(self.container3, text='B4')
# 		self.b5 = Button(self.container3, text='B5')
# 		self.b6 = Button(self.container3, text='B6')
# 		self.b6.pack(side=RIGHT)
# 		self.b4.pack(side=RIGHT)
# 		self.b5.pack(side=RIGHT)

# class Janela:
# 	def __init__(self, toplevel):
# 		self.frame = Frame(toplevel)
# 		self.frame.pack()
# 		self.texto = Label(self.frame, text='Clique para ficar amarelo')
# 		self.texto['width'] = 26
# 		self.texto['height'] = 3
# 		self.texto.pack()
# 		self.botaoverde = Button(self.frame, text='Clique')
# 		self.botaoverde['background'] = 'green'
# 		self.botaoverde.bind("<Button-1>", self.muda_cor) #pode tambem ser simplificado com "<1>"
# 							# "<ButtonRelease-1>"
# 							# "<Motion>"
# 							# "<Leave>"
# 							# "<Double-Button-1>"
# 							# "<Triple-KeyPress-P>"
# 							# "<Any-KeyPress>"
# 							# "<Any-Button>"
# 		self.botaoverde.pack()


# def muda_cor(self, event):
# 	if self.botaoverde['bg'] == 'green':
# 		self.botaoverde['bg'] = 'yellow'
# 		self.texto['text'] = 'Clique para ficar verde'
# 	else:
# 		self.botaoverde['bg'] = 'green'
# 		self.texto['text'] = 'Clique para ficar amarelo'

# class Janela:
# 	def __init__(self, toplevel):
# 		self.frame = Frame(toplevel)
# 		self.frame.pack()
# 		self.frame2 = Frame(toplevel)
# 		self.frame2.pack()
# 		self.titulo = Label(self.frame, text='VIDENTE 2022', font=('Verdana', '13', 'bold'))
# 		self.titulo.pack()
# 		self.msg = Label(self.frame, width=40, height=6, text='Adivinho o evento ocorrido!')
# 		self.msg.focus_force()
# 		self.msg.pack()
# 		# Definindo o botão 1
# 		self.b01 = Button(self.frame2, text='Botão 1')
# 		self.b01['padx'], self.b01['pady'] = 10, 5
# 		self.b01['bg'] = 'deepskyblue'
# 		self.b01.bind("<Return>", self.keypress01)
# 		self.b01.bind("<Any-Button>", self.button01)
# 		self.b01.bind("<FocusIn>", self.fin01)
# 		self.b01.bind("<FocusOut>", self.fout01)
# 		self.b01['relief'] = RIDGE
# 		self.b01.pack(side=LEFT)
# 		# Definindo o botão 2
# 		self.b02 = Button(self.frame2, text='Botão 2')
# 		self.b02['padx'], self.b02['pady'] = 10, 5
# 		self.b02['bg'] = 'deepskyblue'
# 		self.b02.bind("<Return>", self.keypress02)
# 		self.b02.bind("<Any-Button>", self.button02)
# 		self.b02.bind("<FocusIn>", self.fin02)
# 		self.b02.bind("<FocusOut>", self.fout02)
# 		self.b02['relief'] = RIDGE
# 		self.b02.pack(side=LEFT)
#
# 	def keypress01(self, event):
# 		self.msg['text'] = 'ENTER sobre o Botão 1'
#
# 	def keypress02(self, event):
# 		self.msg['text'] = 'ENTER sobre o Botão 2'
#
# 	def button01(self, event):
# 		self.msg['text'] = 'Clique sobre o Botão 1'
#
# 	def button02(self, event):
# 		self.msg['text'] = 'Clique sobre o Botão 2'
#
# 	def fin01(self, event):
# 		self.b01['relief'] = FLAT
#
# 	def fout01(self, event):
# 		self.b01['relief'] = RIDGE
#
# 	def fin02(self, event):
# 		self.b02['relief'] = FLAT
#
# 	def fout02(self, event):
# 		self.b02['relief'] = RIDGE

# class Janela:
# 	def __init__(self, toplevel):
# 		self.frame = Frame(toplevel)
# 		self.frame.pack()
# 		self.b1 = Button(self.frame)
# 		self.b1.bind("<Button-1>", self.press_b1)
# 		self.b1.bind("<ButtonRelease>", self.release_b1)
# 		self.b1['text'] = 'Clique em mim!'
# 		self.b1['width'], self.b1['bg'] = 20, 'brown'
# 		self.b1['fg'] = 'yellow'
# 		self.b1.pack(side=LEFT)
# 		self.b2 = Button(self.frame)
# 		self.b2['width'], self.b2['bg'] = 20, 'brown'
# 		self.b2['fg'] = 'yellow'
# 		self.b2.pack(side=LEFT)
# 		self.b3 = Button(self.frame, command=self.click_b3)
# 		self.b3['width'], self.b3['bg'] = 20, 'brown'
# 		self.b3['fg'] = 'yellow'
# 		self.b3.pack(side=LEFT)
#
# 	def press_b1(self, event):
# 		self.b1['text'] = ''
# 		self.b2['text'] = 'Errou! Estou aqui!'
#
# 	def release_b1(self, event):
# 		self.b2['text'] = ''
# 		self.b3['text'] = 'OOOpa! Mudei de novo!'
#
# 	def click_b3(self):
# 		self.b3['text'] = 'Ok... Você me pegou...'

# class Passwords:
# 	def __init__(self, toplevel):
# 		self.frame1 = Frame(toplevel)
# 		self.frame1.pack()
# 		self.frame2 = Frame(toplevel)
# 		self.frame2.pack()
# 		self.frame3 = Frame(toplevel)
# 		self.frame3.pack()
# 		self.frame4 = Frame(toplevel, pady=10)
# 		self.frame4.pack()
# 		Label(self.frame1, text='PASSWORDS', fg='darkblue', font=('Verdana', '14', 'bold'), height=3).pack()
# 		fonte1 = ('Verdana', '10', 'bold')
# 		Label(self.frame2, text='Nome: ', font=fonte1, width=8).pack(side=LEFT)
# 		self.nome = Entry(self.frame2, width=15, font=fonte1)
# 		self.nome.focus_force()  # Para o foco começar neste campo
# 		self.nome.pack(side=LEFT)
# 		Label(self.frame3, text='Senha: ', font=fonte1, width=8).pack(side=LEFT)
# 		self.senha = Entry(self.frame3, width=15, show='*', font=fonte1)
# 		self.senha.pack(side=LEFT)
# 		self.confere = Button(self.frame4, font=fonte1, text='Conferir', bg='green', command=self.conferir)
# 		self.confere.pack()
# 		self.msg = Label(self.frame4, font=fonte1, height=3, text='AGUARDANDO...')
# 		self.msg.pack()
#
# 	def conferir(self):
# 		NOME = self.nome.get()
# 		SENHA = self.senha.get()
# 		if NOME == SENHA:
# 			self.msg['text'] = 'ACESSO PERMITIDO'
# 			self.msg['fg'] = 'darkgreen'
# 		else:
# 			self.msg['text'] = 'ACESSO NEGADO'
# 			self.msg['fg'] = 'red'
# 			self.nome.focus_force()


# class Kanvas:
# 	def __init__(self, raiz):
# 		self.canvas1 = Canvas(raiz, width=100, height=200, cursor='X_Cursor', bd=50, bg='dodgerblue')
# 		self.canvas1.pack(side=LEFT)
# 		self.canvas2 = Canvas(raiz, width=100, height=200, cursor='circle', bd=50, bg='purple')
# 		self.canvas2.pack(side=LEFT)

# 		tipos de cursor
# "arrow"  # "circle"	# "clock"	# "cross"	# "dotbox"	# "exchange"	# "fleur"
# # "heart"	# "man"		# "mouse"	# "pirate"	# "plus"	# "shuttle" 	# "sizing"
# "spider"	# "spraycan"	# "star"	# "target"	# "tcross"	# "trek"	# "watch" "X_Cursor"

class Linhas:
	def __init__(self, raiz):
		self.canvas = Canvas(raiz, width=400, height=400, cursor='watch', bd=5)
		self.canvas.pack()
		self.frame = Frame(raiz)
		self.frame.pack()
		self.last = [200, 200]
		configs = {'fg': 'darkblue', 'bg': 'ghostwhite', 'relief': GROOVE, 'width': 11, 'font': ('Verdana', '8', 'bold')}
		self.b1 = Button(self.frame, configs, text='Esquerda', command=self.left)
		self.b1.pack(side=LEFT)
		self.b2 = Button(self.frame, configs, text='Para cima', command=self.up)
		self.b2.pack(side=LEFT)
		self.b3 = Button(self.frame, configs, text='Para baixo', command=self.down)
		self.b3.pack(side=LEFT)
		self.b4 = Button(self.frame, configs, text='Direita', command=self.right)
		self.b4.pack(side=LEFT)


	def left(self):  # Desenha um segmento para a esquerda
		x, y = self.last[0] - 10, self.last[1]
		self.canvas.create_line(self.last, x, y, fill='red')
		self.last = [x, y]


	def up(self):  # Desenha um segmento para cima
		x, y = self.last[0], self.last[1] - 10
		self.canvas.create_line(self.last, x, y, fill='red')
		self.last = [x, y]


	def down(self):  # Desenha um segmento para baixo
		x, y = self.last[0], self.last[1] + 10
		self.canvas.create_line(self.last, x, y, fill='red')
		self.last = [x, y]


	def right(self):  # Desenha um segmento para a direita
		x, y = self.last[0] + 10, self.last[1]
		self.canvas.create_line(self.last, x, y, fill='red')
		self.last = [x, y]




raiz = Tk()

Linhas(raiz)

raiz.mainloop()
