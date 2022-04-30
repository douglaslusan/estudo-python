# criando a view

from tkinter import *
from tkinter import ttk
from tkcalendar import Calendar, DateEntry
from tkinter import messagebox
from view import *


# ******************  cores
preto = '#050405'
branco = '#feffff'
verde = '#47af79'
valor = '#38566a'
letra = '#403d3d'
profit = '#e06636'
azul = '#068cfc'
vermelho = '#ef5350'
verdeEscuro = '#273838'
azulClarinho = '#e9edf5'

# ******************  criando janela

janela = Tk()
janela.title('formulario')
janela.geometry('1043x460')
janela.configure(background=azulClarinho)
# janela.resizable(height=False, width=False)

# ******************  criando frames

frame_cima = Frame(janela, width=310, height=50, bg=verde, relief='flat')
frame_cima.grid(row=0, column=0)

frame_baixo = Frame(janela, width=310, height=403, bg=branco, relief='flat')
frame_baixo.grid(row=1, column=0, padx=0, pady=5, sticky=NSEW)

frame_direita = Frame(janela, width=688, height=403, bg=azulClarinho, relief='flat')
frame_direita.grid(row=0, column=1, rowspan=2, padx=5, sticky=NSEW)

# **************** label cima

app_nome = Label(frame_cima, text='Formulário de Consultas', bg=verde, fg=branco,
				 font=('Ivy 13 bold'), relief='flat')
app_nome.place(x=30, y=15)


# variavel global
global arvore

def inserir():
	nome = e_nome.get()
	email = e_email.get()
	fone = e_fone.get()
	data = e_data.get()
	estado = e_estado.get()
	assunto = e_sobre.get()

	lista = [nome, email, fone, data, estado, assunto]

	if nome == '':
		messagebox.showerror('Erro', 'O nome não pode ser vazio')
	elif email == '':
		messagebox.showerror('Erro', 'O email não pode ser vazio')
	elif fone == '':
		messagebox.showerror('Erro', 'O fone não pode ser vazio')
	elif fone.isalpha():
		messagebox.showerror('Erro', 'O fone deve conter somente numeros')
	elif estado == '':
		messagebox.showerror('Erro', 'O estado não pode ser vazio')

	else:
		inserir_info(lista)
		messagebox.showinfo('Sucesso', 'os dados foram inseridos')

		e_nome.delete(0, 'end')
		e_email.delete(0, 'end')
		e_fone.delete(0, 'end')
		e_data.delete(0, 'end')
		e_estado.delete(0, 'end')
		e_sobre.delete(0, 'end')

	for widget in frame_direita.winfo_children():
		widget.destroy()

	mostrar()



def atualizar():
	try:
		treeview_dados = arvore.focus()
		treeview_dicio = arvore.item(treeview_dados)
		treeview_lista = treeview_dicio['values']
		valor_id = treeview_lista[0]

		e_nome.delete(0, 'end')
		e_email.delete(0, 'end')
		e_fone.delete(0, 'end')
		e_data.delete(0, 'end')
		e_estado.delete(0, 'end')
		e_sobre.delete(0, 'end')

		e_nome.insert(0, treeview_lista[1])
		e_email.insert(0, treeview_lista[2])
		e_fone.insert(0, treeview_lista[3])
		e_data.insert(0, treeview_lista[4])
		e_estado.insert(0, treeview_lista[5])
		e_sobre.insert(0, treeview_lista[6])

		def atualizar_dados():
			nome = e_nome.get()
			email = e_email.get()
			fone = e_fone.get()
			data = e_data.get()
			estado = e_estado.get()
			assunto = e_sobre.get()

			lista = [nome, email, fone, data, estado, assunto, valor_id]

			if nome == '':
				messagebox.showerror('Erro', 'O nome não pode ser vazio')
			elif email == '':
				messagebox.showerror('Erro', 'O email não pode ser vazio')
			elif fone == '':
				messagebox.showerror('Erro', 'O fone não pode ser vazio')
			elif fone.isalpha():
				messagebox.showerror('Erro', 'O fone deve conter somente numeros')
			elif estado == '':
				messagebox.showerror('Erro', 'O estado não pode ser vazio')

			else:
				atualizar_info(lista)
				messagebox.showinfo('Sucesso', 'os dados foram atualizados')

				e_nome.delete(0, 'end')
				e_email.delete(0, 'end')
				e_fone.delete(0, 'end')
				e_data.delete(0, 'end')
				e_estado.delete(0, 'end')
				e_sobre.delete(0, 'end')

			for widget in frame_direita.winfo_children():
				widget.destroy()

			mostrar()

		btn_confirmar = Button(frame_baixo, command=atualizar_dados, text='confirmar', width=10, font=('Ivy 8 bold'), bg=azulClarinho,
							relief='raised', overrelief='ridge')
		btn_confirmar.place(x=110, y=360)


	except IndexError:
		messagebox.showerror('Erro', 'Selecione um dado na Tabela')


def deletar():
	try:
		treeview_dados = arvore.focus()
		treeview_dicio = arvore.item(treeview_dados)
		treeview_lista = treeview_dicio['values']
		valor_id = [treeview_lista[0]]

		deletar_info(valor_id)
		messagebox.showinfo('Sucesso', 'Dados deletados da tabela')

		for widget in frame_direita.winfo_children():
			widget.destroy()

		mostrar()

	except IndexError:
		messagebox.showerror('Erro', 'Selecione um dado na Tabela')


# **************** configurando frame baixo

# nome
l_nome = Label(frame_baixo, text='Nome', bg=branco, fg=valor,
				 font=('Ivy 10 bold'), relief='flat')
l_nome.place(x=10, y=10)

e_nome = Entry(frame_baixo, width=48, justify='left', relief='solid')
e_nome.place(x=10, y=35)

# email
l_email = Label(frame_baixo, text='E-mail', bg=branco, fg=valor,
				 font=('Ivy 10 bold'), relief='flat')
l_email.place(x=10, y=70)

e_email = Entry(frame_baixo, width=48, justify='left', relief='solid')
e_email.place(x=10, y=95)

# telefone
l_fone = Label(frame_baixo, text='Telefone', bg=branco, fg=valor,
				 font=('Ivy 10 bold'), relief='flat')
l_fone.place(x=10, y=130)

e_fone = Entry(frame_baixo, width=48, justify='left', relief='solid')
e_fone.place(x=10, y=155)

# data consulta
l_data = Label(frame_baixo, text='Data Nasc', bg=branco, fg=valor, font=('Ivy 10 bold'), relief='flat')
l_data.place(x=10, y=190)

e_data = DateEntry(frame_baixo, width=15, background=branco, foreground=azul, year=2022)
e_data.place(x=10, y=215)

# estado
l_estado = Label(frame_baixo, text='UF:', bg=branco, fg=valor, font=('Ivy 10 bold'), relief='flat')
l_estado.place(x=175, y=190)

e_estado = Entry(frame_baixo, width=20, justify='left', relief='solid')
e_estado.place(x=175, y=215)

# sobre
l_sobre = Label(frame_baixo, text='Sobre', bg=branco, fg=valor, font=('Ivy 10 bold'), relief='flat')
l_sobre.place(x=10, y=250)

e_sobre = Entry(frame_baixo, width=48, justify='left', relief='solid')
e_sobre.place(x=10, y=275)


# ******************* botoes
btn_inserir = Button(frame_baixo, text='Inserir', command=inserir, width=10, font=('Ivy 8 bold'), bg=azulClarinho,
					 relief='raised', overrelief='ridge')
btn_inserir.place(x=10, y=320)

btn_update = Button(frame_baixo, text='Atualizar', command=atualizar, width=10, font=('Ivy 8 bold'), bg=azulClarinho,
					 relief='raised', overrelief='ridge')
btn_update.place(x=110, y=320)

btn_delete = Button(frame_baixo, command=deletar, text='Deletar', width=10, font=('Ivy 8 bold'), bg=azulClarinho,
					relief='raised', overrelief='ridge')
btn_delete.place(x=210, y=320)

#  ********************** lista para cabecalho

def mostrar():


	global arvore
	lista = mostrar_info()

	tabela_head = ['Id','Nome','E-mail','Telefone','Nascimento','Estado','Sobre']


	# ************ criando a tabela *******************
	arvore = ttk.Treeview(frame_direita, selectmode='extended', columns=tabela_head, show='headings')

	# ********* scroll vertical
	vsb = ttk.Scrollbar(frame_direita, orient='vertical', command=arvore.yview)

	# ********* scroll horizontal
	hsb = ttk.Scrollbar(frame_direita, orient='horizontal', command=arvore.xview)

	arvore.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)

	arvore.grid(column=0, row=0, sticky='nsew')
	vsb.grid(column=1, row=0, sticky='ns')
	hsb.grid(column=0, row=1, sticky='ew')

	frame_direita.grid_rowconfigure(0, weight=12)

	hd = ['nw','nw','nw','nw','nw','center','center']
	h = [30, 170, 140, 100, 90, 50, 130]
	n = 0

	for col in tabela_head:
		arvore.heading(col, text=col.title(), anchor='center')
		arvore.column(col, width=h[n], anchor=hd[n])
		n += 1

	for item in lista:
		arvore.insert('', 'end', values=item)

mostrar()


janela.mainloop()
