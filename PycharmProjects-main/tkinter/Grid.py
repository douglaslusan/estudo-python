from tkinter import *

class Griding:
	def __init__(self, raiz):
		self.raiz = raiz
		self.raiz.title('Tchau!')
		Label(self.raiz, text='Nome:').grid(row=1, column=1, sticky=W, pady=3)
		Label(self.raiz, text='Senha:').grid(row=2, column=1, sticky=W, pady=3)
		self.msg = Label(self.raiz, text='Descubra a senha!')
		self.msg.grid(row=3, column=1, columnspan=2)
		self.nome = Entry(self.raiz, width=10)
		self.nome.grid(row=1, column=2, sticky=E + W, pady=3)
		self.nome.focus_force()
		self.senha = Entry(self.raiz, width=10, fg='darkgray', show='l', font=('Wingdings', '10'))
		self.senha.grid(row=2, column=2, sticky=E + W, pady=3)
		self.ok = Button(self.raiz, width=8, command=self.testar, text='OK')
		self.ok.grid(row=4, column=1, padx=2, pady=3)
		self.close = Button(self.raiz, width=8, command=self.fechar, text='Fechar')
		self.close.grid(row=4, column=2, padx=2, pady=3)


	def testar(self):
		if self.nome.get() == self.senha.get()[::-1]:
			self.msg['text'] = 'Senha correta!'

		else: self.msg['text'] = 'Senha incorreta!'

	def fechar(self):
		self.raiz.destroy()


inst = Tk()

Griding(inst)

inst.mainloop()