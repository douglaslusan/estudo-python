from tkinter import *

azul = '#55a'
branco = '#fff'
preto = '#000'
vermelho = '#f55'
amarelo = '#ff8'

def imprimir():
	ap = aparelho.get()
	if ap == 'r':
		print('Radio')
	elif ap == 't':
		print('TeleVisao')
	elif ap == 'p':
		print('Computador')
	else:
		print('selecione um aparelho')

def imprimirCor():
	apC = cor.get()
	if apC == '#F00':
		print('vermelho')
	elif apC == '#0f0':
		print('verde')
	elif apC == '#00f':
		print('azul')
	else:
		print('selecione uma Cor')

app = Tk()
app.title('Radio')
app.geometry('500x300')
app.configure(bg=amarelo)

aparelho = StringVar()
cor = StringVar()

botao1 = Radiobutton(app,text='RADIO', value='r', variable=aparelho)
botao1.pack()

botao2 = Radiobutton(app,text='TV', value='t', variable=aparelho)
botao2.pack()

botao3 = Radiobutton(app,text='PC', value='p', variable=aparelho)
botao3.pack()

Vermelho = Radiobutton(app,text='vermelho', value='#F00', variable=cor)
Vermelho.pack()

Azul = Radiobutton(app,text='verde', value='#0f0', variable=cor)
Azul.pack()

Azul = Radiobutton(app,text='azul', value='#00f', variable=cor)
Azul.pack()

btn = Button(app, text='esporte selecionado', command=imprimir)
btn.pack()

btnCor = Button(app, text='Cor Selecionado', command=imprimirCor)
btnCor.pack()


app.mainloop()