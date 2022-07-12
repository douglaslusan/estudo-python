from tkinter import *

window = Tk()
window.title('meu primeiro programa')
window.minsize(width=600, height=600)
window.config(padx=20, pady=20)

# Label
my_label = Label(text='I am a label', font=('Arial', 24, 'bold'))
my_label.grid(column=0, row=0)

# def button_clicked():
# 	new_text = 'I got clicked'
# 	my_label.config(text=new_text)

def button_clicked():
	new_text = input.get()
	my_label.config(text=new_text)

# buttons
my_button = Button(width=20, text='Click me', command=button_clicked)
my_button.grid(column=1, row=1)

new_button = Button(width=20, text='Click me', command=button_clicked)
new_button.grid(column=2, row=0)

# Entrys

input = Entry()
input.focus()
input.grid(column=3, row=3)

window.mainloop()