from tkinter import *

BACKGROUND_COLOR = "#B1DDC6"

window = Tk()
window.title('Idiomas')
window.config(padx=50, pady=50, background=BACKGROUND_COLOR)


canvas = Canvas(width=800, height=526, background=BACKGROUND_COLOR, highlightthickness=False)
photo_front = PhotoImage(file='images/card_front.png')
photo_back = PhotoImage(file='images/card_back.png')

canvas.create_image(400, 263, image=photo_front)
canvas.create_text(400, 150, text='title', font=('Arial', 40, 'italic'))
canvas.create_text(400, 263, text='word', font=('Arial', 60, 'bold'))
canvas.grid(row=0, column=0, columnspan=2)


photo_x = PhotoImage(file='images/wrong.png')
button_x = Button(image=photo_x, background=BACKGROUND_COLOR)
button_x.grid(row=1, column=0)


photo_v = PhotoImage(file='images/right.png')
button_v = Button(image=photo_v, background=BACKGROUND_COLOR)
button_v.grid(row=1, column=1)

window.mainloop()