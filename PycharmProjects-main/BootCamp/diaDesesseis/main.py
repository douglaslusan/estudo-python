from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
from time import sleep

ligado = True
menu = Menu()
money = MoneyMachine()

machinneOn = True

maquina = CoffeeMaker()
while machinneOn:
	print(menu.get_items())
	opcao = input('O que deseja: ').lower().strip()
	if opcao == 'report':
		maquina.report()
		money.report()
	elif opcao == 'off':
		machinneOn = False
		print('Turning Off ',end='')
		for i in range(5):
			print('.',end='')
			sleep(0.5)
	else:
		drink = menu.find_drink(opcao)
		if drink:
			if maquina.is_resource_sufficient(menu.find_drink(opcao)):
				money.make_payment(drink.cost)
				maquina.make_coffee(menu.find_drink(opcao))

