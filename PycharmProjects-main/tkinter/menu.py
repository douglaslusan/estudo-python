from tkinter import *

def semComando():
	print('')


azul = '#55a'
branco = '#fff'
preto = '#000'
vermelho = '#f55'

app = Tk()

app.title('MENU')
app.geometry('600x400')
app.configure(bg=azul)

barraMenu = Menu(app)
contatos = Menu(barraMenu, tearoff=0)

contatos.add_command(label='NOVO', command=semComando)
contatos.add_command(label='PESQUISAR', command=semComando)
contatos.add_command(label='DELETAR', command=semComando)
contatos.add_separator()
contatos.add_command(label='SAIR', command=quit)
barraMenu.add_cascade(label='Contato', menu=contatos)

menuManutencao = Menu(barraMenu, tearoff=0)
menuManutencao.add_command(label='Arquivo', command=semComando)
barraMenu.add_cascade(label='Manutenção', menu=menuManutencao)

menuSobre = Menu(barraMenu, tearoff=0)
menuSobre.add_command(label='Ajuda', command=semComando)
barraMenu.add_cascade(label='Sobre', menu=menuSobre)

app.config(menu=barraMenu)



app.mainloop()