from tkinter import *
from tkinter import messagebox
import os

caminho = os.path.dirname(__file__)
nomeArquivo = caminho +'\\cadastro.txt'

def gravar():
	arquivo = open(nomeArquivo, 'a')

	arquivo.write(f'Nome: {text1.get()}')

	arquivo.write(f'\nCPF: {text2.get()}')

	arquivo.write(f'\nTELEFONE: {text3.get()}')

	arquivo.write('\n\n')
	arquivo.close()


def resetCB(): #pode ser usado para limpar dados
	res = messagebox.askyesno('resetar', 'confirma')
	if(res == True):
		text1.delete(0, END)
		text2.delete(0, END)
		text3.delete(0, END)
		text1.focus_force()
		# messagebox.askyesno()
		# messagebox.askokcancel()
		# messagebox.askquestion()
		# messagebox.askretrycancel()
		# messagebox.askyesnocancel()



azul = '#336'
branco = '#fff' #BRANCO
preto = '#000' #PRETO

app = Tk()
app.title("CADASTRO")
app.geometry('500x300')
app.configure(bg=azul)

lb1 = Label(app,text='NOME', bg=branco, fg=preto, anchor=CENTER)
lb1.place(x=10, y=10, width=100, height=30)
text1 = Entry(app)
text1.place(x=120, y=10, width=300, height=30)

lb1 = Label(app,text='CPF', bg=branco, fg=preto, anchor=CENTER)
lb1.place(x=10, y=50, width=100, height=30)
text2 = Entry(app)
text2.place(x=120, y=50, width=300, height=30)

lb1 = Label(app,text='TELEFONE', bg=branco, fg=preto, anchor=CENTER)
lb1.place(x=10, y=90, width=100, height=30)
text3 = Entry(app)
text3.place(x=120, y=90, width=300, height=30)

btnreset = Button(app, text = 'Limpar Campos', command=resetCB)
btnreset.place(x=10, y=130, width=410, height=30)


btn = Button(app, text = 'Gravar em arquivo', command=gravar)
btn.place(x=10, y=170, width=410, height=30)



app.mainloop()