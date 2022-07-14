from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#55ff55"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 

def reset_timer():
	window.after_cancel(timer)
	canvas.itemconfig(timer_text, text='00:00')
	label_timer.config(text='TIMER')
	label_check.config(text='')
	global reps
	reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- # 


def start_timer():
	global reps
	work_sec = WORK_MIN * 60
	short_break_sec = SHORT_BREAK_MIN * 60
	long_break_sec = LONG_BREAK_MIN * 60
	reps += 1
	if reps % 8 == 0:
		count_down(long_break_sec)
		label_timer.config(text='BREAK', foreground=RED)
	elif reps % 2 == 0:
		count_down(short_break_sec)
		label_timer.config(text='BREAK', foreground=PINK)
	else:
		count_down(work_sec)
		label_timer.config(text='WORK', foreground=GREEN)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #


def count_down(count):
	count_min = math.floor(count / 60)
	count_sec = count % 60
	if count_sec < 10:
		count_sec = f'0{count_sec}'

	canvas.itemconfig(timer_text, text=f'{count_min}:{count_sec}')
	if count > 0:
		global timer
		timer = window.after(1000, count_down, count - 1)
	else:
		label_check.config(text='✔' * reps)
		start_timer()


# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.minsize(300, 300)
window.config(padx=100, pady=50, bg=YELLOW)
window.title('POMODORO')


canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato = PhotoImage(file='tomato.png')
canvas.create_image(100, 112, image=tomato)
timer_text = canvas.create_text(100, 132, text='00:00', font=(FONT_NAME, 38, 'bold'), fill='white')
canvas.grid(column=1, row=1)

label_timer = Label(text='TIMER', font=(FONT_NAME, 40, 'bold'), bg=YELLOW, foreground=GREEN)
label_timer.grid(column=1, row=0)

start_button = Button(text='Start', highlightthickness=0, command=start_timer)
start_button.grid(column=0, row=2)

reset_button = Button(text='Reset', highlightthickness=0, command=reset_timer)
reset_button.grid(column=2, row=2)

label_check = Label(foreground=GREEN, bg=YELLOW, font=(FONT_NAME, 10, 'bold'))
label_check.grid(column=1, row=3)

window.mainloop()
