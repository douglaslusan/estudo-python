import time
MENU = {"espresso": {"ingredients": {"water": 50,"coffee": 18,},"cost": 1.5,},
	"latte": {
		"ingredients": {
			"water": 200,
			"milk": 150,
			"coffee": 24,
		},
		"cost": 2.5,
	},
	"cappuccino": {
		"ingredients": {
			"water": 250,
			"milk": 100,
			"coffee": 24,
		},
		"cost": 3.0,
	}
}

profit = 0
resources = {
	"water": 300,
	"milk": 200,
	"coffee": 100,
}


def is_resource_sufficient(order_ingredients):
	"""Retorna True quando o pedido pode ser feito, False se os ingredientes forem insuficientes."""
	for item in order_ingredients:
		if order_ingredients[item] > resources[item]:
			print(f"​desculpe, não há {item} suficiente.")
			return False
	return True


def process_coins():
	"""Retorna o total calculado a partir das moedas inseridas."""
	print("por favor, insira moedas.")
	total = int(input("Quantidade de 0,25?: ")) * 0.25
	print(f'Total: ${total}')
	total += int(input("Quantidade de 0,10?: ")) * 0.1
	print(f'Total: ${total}')
	total += int(input("Quantidade de 0,05?: ")) * 0.05
	print(f'Total: ${total}')
	total += int(input("Quantidade de 0,01: ")) * 0.01
	print(f'Total: ${total}')
	return total


def is_transaction_successful(money_received, drink_cost):
	"""Retorna True quando o pagamento for aceito, ou False se o dinheiro for insuficiente."""
	if money_received >= drink_cost:
		change = round(money_received - drink_cost, 2)
		print(f"Aqui está ${change} de troco.")
		global profit
		profit += drink_cost
		return True
	else:
		print("Desculpe, Não há dinheiro suficiente, devolvendo Moedas")
		return False


def make_coffee(drink_name, order_ingredients):
	"""diminua os ingredientes usados dos recursos."""
	for item in order_ingredients:
		resources[item] -= order_ingredients[item]
	print(f"Aqui está sua bebida {drink_name} ☕️. Aproveite!")



is_on = True

while is_on:
	print('*'*50)
	for k, v in MENU.items():
		print(f'{k:10} {"."*20} $ {v["cost"]}')
		time.sleep(0.5)
	print()
	time.sleep(0.3)
	choice = input("​O que gostaria? (espresso/latte/cappuccino): ")
	if choice == "off":
		is_on = False
	elif choice == "report":
		print(f"Agua: {resources['water']}ml")
		print(f"Leite: {resources['milk']}ml")
		print(f"Café: {resources['coffee']}g")
		print(f"Dinheiro: ${profit}")
	elif choice == 'recharge':
		resources = {
			"water": 300,
			"milk": 200,
			"coffee": 100,
		}
	else:
		drink = MENU[choice]
		if is_resource_sufficient(drink["ingredients"]):
			payment = process_coins()
			if is_transaction_successful(payment, drink["cost"]):
				make_coffee(choice, drink["ingredients"])