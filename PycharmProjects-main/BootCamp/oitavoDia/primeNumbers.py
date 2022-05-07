# Write your code below this line 👇

def prime_checker(number):
	div = 1

	for n in range(2, number+1):
		if number % n == 0:
			div += 1
			if div == 2 and n == number:
				print('é primo')
			elif div > 2 and n == number:
				print('nao é primo')

# Write your code above this line 👆

# Do NOT change any of the code below👇
n = int(input("Check this number: "))
prime_checker(number=n)