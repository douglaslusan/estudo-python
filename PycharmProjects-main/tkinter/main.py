from tkinter import *


app = Tk() #instanciar a classe
app.title('Douglas') #colocar titulo na janela
app.geometry('800x600') #tamanho padrao da janela
app.configure(background='#358') #configurar cores

txt1 = Label(app, text='NOME', bg='#520', fg='#000') #CRIAR LABEL
txt1.place(x=30, y=30, width=100, height=30) #COLOCAR LABEL

branco = '#fff' #BRANCO
preto = '#000' #PRETO

txt2 = Label(app, text='OUTRO LABEL', bg=branco, fg=preto)
txt2.pack(ipadx=20, ipady=20, padx=100, pady=10, side='top',fill=X, expand=True) #contains


app.mainloop()

