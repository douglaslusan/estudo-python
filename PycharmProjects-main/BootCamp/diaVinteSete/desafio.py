from tkinter import *

window = Tk()
window.title('conversor Mile to Km')
window.minsize(300, 160)
window.resizable(width=False, height=False)
window.config(padx=10, pady=30, background='lightblue')

entry = Entry(width=10)
entry.focus()
entry.grid(column=1, row=0)

mile_label = Label(text='Miles', font=('Arial', 15, 'bold'), padx=10, pady=10, background='lightblue')
mile_label.grid(column=2, row=0)

is_equal = Label(text='is equal to', font=('Arial', 15, 'bold'), padx=10, pady=10, background='lightblue')
is_equal.grid(column=0, row=1)

result = Label(text='0', font=('Arial', 15, 'bold'), padx=10, pady=10, background='lightblue')
result.grid(column=1, row=1)

km = Label(text='Km', font=('Arial', 15, 'bold'), padx=10, pady=10, background='lightblue')
km.grid(column=2, row=1)

def calcular():
	res = float(entry.get()) * 1.609
	result.config(text=f'{round(res, 2)}')

button = Button(text='Calculate',width=10, command=calcular, padx=10, pady=10)
button.grid(column=1, row=2)

window.mainloop()