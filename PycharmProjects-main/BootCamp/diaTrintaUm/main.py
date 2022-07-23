from tkinter import *
from random import choice
import pandas as pd

BACKGROUND_COLOR = "#B1DDC6"
dict_random = {}
to_learn = {}

try:
	data = pd.read_csv('data/words_to_learn.csv')
except FileNotFoundError:
	original_data = pd.read_csv('data/palavras.csv')
	to_learn = original_data.to_dict(orient='records')
else:
	to_learn = data.to_dict(orient='records')


def random_word():
	global dict_random, flip
	window.after_cancel(flip)
	dict_random = choice(to_learn)
	canvas.itemconfig(word_title, text='English', fill='black')
	canvas.itemconfig(word_english, text=dict_random['ingles'], fill='black')
	canvas.itemconfig(canvas_imagem, image=photo_front)
	flip = window.after(3000, func=flip_card)

def flip_card():
	canvas.itemconfig(canvas_imagem, image=photo_back)
	canvas.itemconfig(word_title, text='Portugues', fill='white')
	canvas.itemconfig(word_english, text=dict_random['portugues'], fill='white')

def word_known():
	to_learn.remove(dict_random)
	data = pd.DataFrame(to_learn)
	print(len(to_learn))
	data.to_csv('data/words_to_learn.csv', index=False)
	random_word()

window = Tk()
window.title('Idiomas')
window.config(padx=50, pady=50, background=BACKGROUND_COLOR)

flip = window.after(3000, func=flip_card)

canvas = Canvas(width=800, height=526, background=BACKGROUND_COLOR, highlightthickness=False)
photo_front = PhotoImage(file='images/card_front.png')
photo_back = PhotoImage(file='images/card_back.png')


canvas_imagem = canvas.create_image(400, 263, image=photo_front)
word_title = canvas.create_text(400, 150, text='', font=('Arial', 40, 'italic'))
word_english = canvas.create_text(400, 263, text='', font=('Arial', 60, 'bold'))
canvas.grid(row=0, column=0, columnspan=2)


photo_x = PhotoImage(file='images/wrong.png')
button_x = Button(image=photo_x, background=BACKGROUND_COLOR, command=random_word)
button_x.grid(row=1, column=0)


photo_v = PhotoImage(file='images/right.png')
button_v = Button(image=photo_v, background=BACKGROUND_COLOR, command=word_known)
button_v.grid(row=1, column=1)

random_word()

window.mainloop()