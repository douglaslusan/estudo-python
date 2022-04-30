from tkinter import *

azul = '#55a'
branco = '#fff'
preto = '#000'
vermelho = '#f55'
amarelo = '#ff8'

def imprimir():
	ap = aparelho.get()
	if ap == 'Radio':
		print('Radio')
	elif ap == 'TV':
		print('TeleVisao')
	elif ap == 'PC':
		print('Computador')
	else:
		print('selecione um aparelho')


app = Tk()
app.title('Radio')
app.geometry('500x300')
app.configure(bg=vermelho)

listaAparelho = ['Radio', 'TV', 'PC']

aparelho = StringVar()
aparelho.set(listaAparelho[0]) #valor padrao

botao1 = Label(app,text='APARELHOS')
botao1.pack()

op = OptionMenu(app, aparelho, *listaAparelho)
op.pack()

btn = Button(app, text='esporte selecionado', command=imprimir)
btn.pack()


app.mainloop()