#!/usr/bin/python3

'''
Looping

Functions
'''

x = 0
for x in range(1,5):
	print(x)
	x += 3
	print(x)

x = 0
while x < 5:
	print(x)
	x += 3


def sub(x):
	x -= 5
	return x

'''
Case Study: Determine if a number is prime, or not
'''

def is_prime(number):
	prime = True
	if number < 2:
		prime = False
	elif number < 4:
		prime = True

	for x in range(4, number):
		if x % number == 0:
			prime = False
	# if the number is prime or not
	# Print So
	if prime:
		print(number, "is prime!")
	else:
		print(number, "is not prime.")

if __name__ == '__main__':
	print(sub(5))
	from helper import addition
	print(addition(7, 944))
	is_prime(4471)
