from tkinter import *
from tkinter import messagebox

azul = '#55a'
branco = '#fff'
preto = '#000'
vermelho = '#f55'
amarelo = '#ff8'
violeta = '#a0f'


def mostrarMsg(tipomsg, msg):
	if (tipomsg == '1'):
		messagebox.showinfo(title='TKINTER CURSO', message=msg)
	elif (tipomsg == '2'):
		messagebox.showwarning(title='TKINTER CURSO', message=msg)
	if (tipomsg == '3'):
		messagebox.showerror(title='TKINTER CURSO', message=msg)

def resetCB(): #pode ser usado para limpar dados
	res = messagebox.askyesno('resetar', 'confirma')
	if(res == True):
		caixa.delete(0, END)
		caixa.insert(0, '')
		# messagebox.askyesno()
		# messagebox.askokcancel()
		# messagebox.askquestion()
		# messagebox.askretrycancel()
		# messagebox.askyesnocancel()


app = Tk()
app.title('Mensagem Box')
app.geometry('500x300')
app.configure(bg=violeta)

numCx = StringVar()
vmsg = 'clique OK'

caixa = Entry(app, textvariable=numCx)

caixa.pack()


Button(app, text='mostra mensagem', command=lambda: mostrarMsg(numCx.get(), vmsg)).pack()

Button(app, text='resetar Mensagem', command=resetCB).pack()

app.mainloop()
