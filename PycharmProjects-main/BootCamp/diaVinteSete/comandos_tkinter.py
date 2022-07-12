from tkinter import *

window = Tk()
window.title('meu primeiro programa')
window.minsize(width=600, height=600)

# Label
my_label = Label(text='I am a label', font=('Arial', 24, 'bold'))
my_label.pack()

# def button_clicked():
# 	new_text = 'I got clicked'
# 	my_label.config(text=new_text)

def button_clicked():
	new_text = input.get()
	my_label.config(text=new_text)

# buttons
my_button = Button(width=20, text='Click me', command=button_clicked)
my_button.pack()

# Entrys

input = Entry()
input.insert(END, string='email: ')
input.focus()
input.pack(pady=10)

# textBOX

text = Text(width=30, height=10)
text.insert(END, 'exemplo de entrada de texto de multi linha')
# pega o valor do text da linha 1 caracter 0
print(text.get('1.0', END))
text.pack()

# spinBox
def spinbox_used():
	print(spin_box.get())


spin_box = Spinbox(from_= 0, to= 10, width=5, command=spinbox_used)
spin_box.pack()

# scale botao deslizante

def scale_used(value):
	print(value)

scale = Scale(from_=0, to=100, width=20, orient='horizontal', command=scale_used)
scale.pack()

# checkbox

def check_button_used():
	print(checked_state.get())

checked_state = IntVar()
check_button = Checkbutton(text='Is ON?', variable=checked_state, command=check_button_used)
check_button.pack()

# radio box
def radio_used():
	print(f'option: {radio_state.get()}')

radio_state = IntVar()
radio_button1 = Radiobutton(text='option 1', value=1, variable=radio_state, command=radio_used)
radio_button2 = Radiobutton(text='option 2', value=2, variable=radio_state, command=radio_used)
radio_button1.pack()
radio_button2.pack()

# listBox
def listbox_used(event):
	print(listbox.get(listbox.curselection()))

fruits = ['maca', 'melancia', 'uva', 'limao', 'abacate']
listbox = Listbox(height=len(fruits))
for item in fruits:
	listbox.insert(fruits.index(item), item)

listbox.bind('<<ListboxSelect>>', listbox_used)
listbox.pack()

window.mainloop()