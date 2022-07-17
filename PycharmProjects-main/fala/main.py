import pyttsx3

engine = pyttsx3.init()
name = input('digite seu nome: ')
comida = input('a que gosta de comer: ')
engine.say(f' {name} gosta de {comida}')

engine.runAndWait()
