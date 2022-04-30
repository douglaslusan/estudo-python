from tkinter import *

# --------- cores -----------------
preto = "#000000"
branco = "#f1f1f1"
verde = "#004338"

# criando a janela -----------------

janela = Tk()
janela.title('Paleta de Cores')
janela.geometry("550x220")
janela.configure(bg="#234766")
janela.resizable(width=False, height=False)
janela.iconphoto(False, PhotoImage(file='cores.png'))

# configurando a janela -----------------

tela = Label(janela, bg=preto, width=40, height=10, bd=5)
tela.grid(row=0, column=0)

frame_direita = Frame(janela, bg="#234766", width=100, padx=5)
frame_direita.grid(row=0, column=1)

frame_baixo = Frame(janela, bg="#234766")
frame_baixo.grid(row=1, column=0, columnspan=2, pady=15)


# Funcao scale
def escala(valor):
	r = slider_red.get()
	g = slider_green.get()
	b = slider_blue.get()

	hexad = "#%02x%02x%02x" % (r, g, b)

	# alterando a cor da paleta
	tela['bg'] = hexad

	# alterando a entry
	e_cor.delete(0, END)
	e_cor.insert(0, hexad)


# Funcao clicar
def on_clic():
	clip = Tk()
	clip.withdraw()
	clip.clipboard_clear()
	clip.clipboard_append(e_cor.get())
	clip.destroy()


# configurando o frame direito -----------------

red = Label(frame_direita, text='RED', width=7, bg=branco, fg='red', anchor='nw',
			font=('arial', 12, 'bold'))
red.grid(row=0, column=0)

# slider vermelho
slider_red = Scale(frame_direita, command=escala, from_=0, to=255, length=150, bg=branco,
				   fg='red', orient=HORIZONTAL)
slider_red.grid(row=0, column=1)

green = Label(frame_direita, text='GREEN', width=7, bg=branco, fg='green', anchor='nw',
			font=('arial', 12, 'bold'))
green.grid(row=1, column=0)

# slider verde
slider_green = Scale(frame_direita, command=escala, from_=0, to=255, length=150, bg=branco, fg='green',
					 orient=HORIZONTAL)
slider_green.grid(row=1, column=1)

blue = Label(frame_direita, text='BLUE', width=7, bg=branco, fg='blue', anchor='nw',
			font=('arial', 12, 'bold'))
blue.grid(row=2, column=0)

# slider azul
slider_blue = Scale(frame_direita, command=escala, from_=0, to=255, length=150, bg=branco,
			fg='blue', orient=HORIZONTAL)
slider_blue.grid(row=2, column=1)

# configurando o frame baixo -----------------
rgb = Label(frame_baixo, text='RGB', bg=branco, font=('Ivy', 10, 'bold'))
rgb.grid(row=0, column=0, padx=5)

# Entry -------------------
e_cor = Entry(frame_baixo, width=20, font=('Ivy', 10, 'bold'), justify=CENTER)
e_cor.grid(row=0, column=1, padx=5)

# APP NOME ----------------
nome = Label(frame_baixo, text='Cod. Hex', bg=branco, font=('Arial', 15, 'bold'))
nome.grid(row=0, column=2, padx=4)

# botao copiar ----------------
btn = Button(frame_baixo, text='Copiar', command=on_clic, bg='#bdbdbd', font=('Ivy', 8, 'bold'),
			 relief=RAISED, overrelief=RIDGE)
btn.grid(row=0, column=3, padx=5)

janela.mainloop()
