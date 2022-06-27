from turtle import Turtle, Screen
import random
screen = Screen()

def draw_spirograph(size):
	for i in range(int(360 / size)):
		bob.circle(140)
		bob.pencolor(random_color())
		bob.rt(size)

def random_color():
	r = random.randint(0, 200)
	g = random.randint(0, 200)
	b = random.randint(0, 200)
	tup = (r, g, b)
	return tup

bob = Turtle()
bob.shape('turtle')
screen.colormode(255)
bob.pensize(10)
bob.speed(0)
screen.screensize(800, 800)

lado = 3
tamanho = 80

total = 0
# while lado < 15:
# 	tup = random_color()
# 	raio = 360 / lado
# 	bob.pencolor(tup)
# 	for i in range(lado):
# 		bob.fd(tamanho)
# 		bob.lt(raio)
# 	lado += 1


lados = [90, 270]
while total < 3000:
	passos = random.randint(20, 80)
	raio = random.randint(10, 350)
	bob.pencolor(random_color())
	bob.fd(passos)
	bob.lt(raio)
	total += passos


# draw_spirograph(5)


screen.exitonclick()
