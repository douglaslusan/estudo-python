from tkinter import *
from tkinter import messagebox
from random import randint, choice, shuffle
import pyperclip


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
	letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
			   'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
			   'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
	numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
	symbols = ['!', '#', '$', '%', '&', '*', '+']

	password_letters = [choice(letters) for _ in range(randint(8, 10))]
	password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
	password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

	password_list = password_letters + password_symbols + password_numbers
	shuffle(password_list)

	password = "".join(password_list)
	entry_Pass.insert(0, password)
	pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #


def save():
	web = entry_web.get()
	email = entry_email.get()
	password = entry_Pass.get()

	if len(web) == 0 or len(email) == 0 or len(password) == 0:
		messagebox.showinfo(title='Oops', message="please don't leave any fields empty!")
	else:
		is_yes = messagebox.askyesno(title='Confirm', message=f'web: {web}\nemail: {email}\npassword: {password}')
		if is_yes:
			with open('data.txt', 'a') as file:
				file.write(f'{web} | {email} | {password}\n')
				entry_web.delete(0, END)
				entry_Pass.delete(0, END)
				entry_web.focus()


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title('passwords generator')
window.config(pady=50, padx=50)

canvas = Canvas(height=200, width=200)
logo = PhotoImage(file='logo.png')
canvas.create_image(100, 100, image=logo)
canvas.grid(column=1, row=0)

# labels
label_website = Label(text='Website:', pady=10)
label_website.grid(column=0, row=1, padx=10)

label_Email_user = Label(text='Email/Username:')
label_Email_user.grid(column=0, row=2, padx=10)

label_password = Label(text='Password:', pady=10, padx=10)
label_password.grid(column=0, row=3, padx=10)

# entries

entry_web = Entry(width=32)
entry_web.grid(column=1, row=1, sticky='ew')
entry_web.focus()

entry_email = Entry(width=50)
entry_email.insert(0, 'douglas.lusan@gmail.com')
entry_email.grid(column=1, row=2, columnspan=2, sticky='ew')

entry_Pass = Entry(width=32)
entry_Pass.grid(row=3, column=1, sticky='ew')

# buttons
button_search = Button(text='Search')
button_search.grid(row=1, column=2, padx=10, sticky='ew')

button_generate = Button(text='Generate Password', command=generate_password)
button_generate.grid(row=3, column=2, sticky='ew', padx=10)

button_add = Button(text='Add', command=save)
button_add.grid(row=4, column=1, columnspan=2, sticky='ew', padx=10)

window.mainloop()
