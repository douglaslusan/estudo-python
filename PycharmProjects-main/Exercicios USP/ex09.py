n = int(input('digite um numero: '))
if n < 1:
	print(n)
elif n % 3 == 0 and n % 5 == 0:
	print('FizzBuzz')
elif n % 3 == 0:
	print('Fizz')
elif n % 5 == 0:
	print('Buzz')
else:
	print(n)