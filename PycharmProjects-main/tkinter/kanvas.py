from tkinter import *
from time import localtime


class Kanvas:
	def __init__(self, raiz):
		self.canvas1 = Canvas(raiz, width=100, height=200, cursor='X_Cursor', bd=50, bg='dodgerblue')
		self.canvas1.pack(side=LEFT)
		self.canvas2 = Canvas(raiz, width=100, height=200, cursor='circle', bd=50, bg='purple')
		self.canvas2.pack(side=LEFT)

		# tipos de cursor
# "arrow"  # "circle"	# "clock"	# "cross"	# "dotbox"	# "exchange"	# "fleur"
# "heart"	# "man"		# "mouse"	# "pirate"	# "plus"	# "shuttle" 	# "sizing"
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


class SPFC:
	def __init__(self, raiz):
		self.canvas = Canvas(raiz, width=200, height=200, bg='dodgerblue')

		self.canvas.pack()
		altura = 200  # Altura do canvas
		pol = self.canvas.create_polygon
		ret = self.canvas.create_rectangle
		pol(100, altura - 10,
			10, altura - 145,
			10, altura - 190,
			190, altura - 190,
			190, altura - 145,
			100, altura - 10, fill='white')

		ret(15, altura - 147, 185, altura - 185, fill='black')

		pol(20, altura - 140,
			95, altura - 140,
			95, altura - 30,
			20, altura - 140, fill='red')

		pol(105, altura - 30,
			105, altura - 140,
			180, altura - 140,
			105, altura - 30, fill='black')

		self.canvas.create_text(100, altura - 167.5, text='S P F C',
								font=('Arial', '26', 'bold'),
								anchor=CENTER, fill='white')


class Fatias:
	def __init__(self, raiz):
		self.canvas = Canvas(raiz, width=200, height=200)
		self.canvas.pack()
		self.frame = Frame(raiz)
		self.frame.pack()
		self.altura = 200  # Altura do canvas
		self.canvas.create_oval(25, self.altura - 25, 175, self.altura - 175,
				fill='deepskyblue', outline='darkblue')
		fonte = ('Comic Sans MS', '14', 'bold')
		Label(self.frame, text='Fatia: ', font=fonte, fg='blue').pack(side=LEFT)
		self.porcentagem = Entry(self.frame, fg='red', font=fonte, width=5)
		self.porcentagem.focus_force()
		self.porcentagem.pack(side=LEFT)
		Label(self.frame, text='%', font=fonte, fg='blue').pack(side=LEFT)
		self.botao = Button(self.frame, text='Desenhar', command=self.cortar, font=fonte,
				fg='darkblue', bg='deepskyblue')
		self.botao.pack(side=LEFT)


	def cortar(self):
		arco = self.canvas.create_arc
		fatia = float(self.porcentagem.get()) * 359.9 / 100.
		arco(25, self.altura - 25, 175, self.altura - 175,
		fill = 'yellow', outline = 'red', extent = fatia)
		self.porcentagem.focus_force()



class Horas:
	def __init__(self, raiz):
		self.canvas = Canvas(raiz, width=300, height=100)
		self.canvas.pack()
		self.frame = Frame(raiz)
		self.frame.pack()
		self.altura = 100  # Altura do canvas
		# Desenho do relógio-----------------------------
		pol = self.canvas.create_polygon
		ret = self.canvas.create_rectangle
		self.texto = self.canvas.create_text
		self.fonte = ('BankGothic Md BT', '20', 'bold')
		pol(10, self.altura - 10,
			40, self.altura - 90,
			260, self.altura - 90,
			290, self.altura - 10, fill='darkblue')

		pol(18, self.altura - 15,
			45, self.altura - 85,
			255, self.altura - 85,
			282, self.altura - 15, fill='dodgerblue')

		ret(45, self.altura - 35,
			90, self.altura - 60, fill='darkblue', outline='')

		ret(110, self.altura - 35,
			155, self.altura - 60, fill='darkblue', outline='')

		ret(175, self.altura - 35,
			220, self.altura - 60, fill='darkblue', outline='')

		self.texto(100, self.altura - 50, text=':', font=self.fonte, fill='yellow')
		self.texto(165, self.altura - 50, text=':', font=self.fonte, fill='yellow')
		# Fim do desenho do relógio-----------------------

		self.mostrar = Button(self.frame, text='Que horas são?',
							  command=self.mostra,
							  font=('Comic Sans MS', '11', 'bold'),
							  fg='darkblue', bg='deepskyblue')

		self.mostrar.pack(side=LEFT)

	def mostra(self):
		self.canvas.delete('digitos_HORA')
		self.canvas.delete('digitos_MIN')
		self.canvas.delete('digitos_SEG')
		HORA = str(localtime()[3])
		MINUTO = str(localtime()[4])
		SEGUNDO = str(localtime()[5])

		self.texto(67.5, self.altura - 47, text=HORA, fill='red', font=self.fonte, tag='digitos_HORA')

		self.texto(132.5, self.altura - 47, text=MINUTO, fill='red', font=self.fonte, tag='digitos_MIN')

		self.texto(197.5, self.altura - 47, text=SEGUNDO, fill='red', font=self.fonte, tag='digitos_SEG')


class Pacman:
	def __init__(self, raiz):
		self.canvas = Canvas(raiz, height=200, width=200, takefocus=1, bg='deepskyblue', highlightthickness=0)
		self.canvas.bind('<Left>', self.esquerda)
		self.canvas.bind('<Right>', self.direita)
		self.canvas.bind('<Up>', self.cima)
		self.canvas.bind('<Down>', self.baixo)
		self.canvas.focus_force()
		self.canvas.pack()
		# Desenho da carinha
		self.canvas.create_oval(90, 90, 120, 120, tag='bola', fill='yellow')
		self.canvas.create_oval(93, 100, 98, 95, tag='bola', fill='blue')
		self.canvas.create_oval(102, 100, 107, 95, tag='bola', fill='blue')
		self.canvas.create_arc(92, 87, 108, 107, tag='bola', start=220, extent=100, style=ARC)

	# Fim do desenho da carinha

	def esquerda(self, event): self.canvas.move('bola', -10, 0)

	def direita(self, event): self.canvas.move('bola', 10, 0)

	def cima(self, event): self.canvas.move('bola', 0, -10)

	def baixo(self, event): self.canvas.move('bola', 0, 10)


class Palheta:
	def __init__(self, raiz):
		raiz.title("Palheta")
		self.canvas = Canvas(raiz, width=200, height=200)
		self.canvas.pack()
		self.frame = Frame(raiz)
		self.frame.pack()
		self.canvas.create_oval(15, 15, 185, 185, fill='white', tag='bola')
		Label(self.frame, text='Vermelho: 0/255 ').pack(side=LEFT)
		self.vermelho = Entry(self.frame, width=4)
		self.vermelho.focus_force()
		self.vermelho.pack(side=LEFT)
		Label(self.frame, text='Verde: 0/255').pack(side=LEFT)
		self.verde = Entry(self.frame, width=4)
		self.verde.pack(side=LEFT)
		Label(self.frame, text='Azul: 0/255').pack(side=LEFT)
		self.azul = Entry(self.frame, width=4)
		self.azul.pack(side=LEFT)
		Button(self.frame, text='Mostrar', command=self.misturar).pack(side=LEFT)
		self.rgb = Label(self.frame, text='', width=8, font=('Verdana', '10', 'bold'))
		self.rgb.pack()

	def misturar(self):
		cor = "#%02x%02x%02x" % (int(self.vermelho.get()), int(self.verde.get()), int(self.azul.get()))
		self.canvas.delete('bola')
		self.canvas.create_oval(15, 15, 185, 185, fill=cor, tag='bola')
		self.rgb['text'] = cor
		self.vermelho.focus_force()


class AutoCADE:
	def __init__(self, raiz):
		raiz.title('AutoCADÊ')
		self.canvas = Canvas(raiz, width=300, height=300, bg='#beff8c', cursor='hand2')
		self.canvas.bind('<1>', self.desenhar)
		self.canvas.pack()


	def desenhar(self, event):
		x_origem = self.canvas.winfo_rootx()
		y_origem = self.canvas.winfo_rooty()
		x_abs = self.canvas.winfo_pointerx()
		y_abs = self.canvas.winfo_pointery()
		try:
			P = (x_abs - x_origem, y_abs - y_origem)
			self.canvas.create_line(self.ultimo_P, P)
			self.ultimo_P = P
			print(P)
		except:
			self.ultimo_P = (x_abs - x_origem, y_abs - y_origem)



class Palheta2:
	def __init__(self, raiz):
		raiz.title('Palheta Gráfica')
		self.canvas = Canvas(raiz, width=200, height=250)
		self.canvas.bind('<1>', self.misturar)
		self.canvas.bind('<3>', self.voltar)
		self.canvas.pack()
		bola = self.canvas.create_oval
		bola(20, 180, 70, 130, fill='red', outline='')
		bola(75, 180, 125, 130, fill='green', outline='')
		bola(130, 180, 180, 130, fill='blue', outline='')
		bola(45, 120, 155, 10, fill='white', outline='', tag='bola')
		self.tom = [0, 0, 0]


	def misturar(self, event):
		xo = self.canvas.winfo_rootx()
		yo = self.canvas.winfo_rooty()
		xa = self.canvas.winfo_pointerx()
		ya = self.canvas.winfo_pointery()
		cor = self.canvas.find_closest(xa - xo, ya - yo)[0]
		self.tom[cor - 1] = self.tom[cor - 1] + 10
		for i in range(2):
			if self.tom[i] > 255:
				self.tom[i] = 255

		cor = "#%02x%02x%02x" % (self.tom[0], self.tom[1], self.tom[2])
		self.canvas.delete('bola')
		self.canvas.create_oval(45, 120, 155, 10, fill=cor,	outline='', tag='bola')
		print(cor)

	def voltar(self, event):
		xo = self.canvas.winfo_rootx()
		yo = self.canvas.winfo_rooty()
		xa = self.canvas.winfo_pointerx()
		ya = self.canvas.winfo_pointery()
		cor = self.canvas.find_closest(xa - xo, ya - yo)[0]
		self.tom[cor - 1] = self.tom[cor - 1] - 10
		for i in range(2):
			if self.tom[i] < 0:
				self.tom[i] = 0

		cor = "#%02x%02x%02x" % (self.tom[0], self.tom[1], self.tom[2])
		self.canvas.delete('bola')
		self.canvas.create_oval(45, 120, 155, 10, fill=cor,	outline='', tag='bola')
		print(cor)


inst = Tk()

Horas(inst)

inst.mainloop()
