# Write your code below this line 👇

def prime_checker(number):
	ePrimo = True
	for n in range(2, number):
		if number % n == 0:
			ePrimo = False
	if ePrimo:
		print('é primo')
	else:
		print('nao é primo')
# Write your code above this line 👆

# Do NOT change any of the code below👇
n = int(input("Check this number: "))
prime_checker(number=n)