#!/bin/usr/python3

# Modular code

# Basic addition function
def add(a, b):
	return a+b

# Recurseive Factorial Function
def factorial(n):
    if n <= 0:
        return 1
    else:
        return n * factorial(n-1)

# Variable scope
# We will calculate e through the Newton's Formulea
#     infinity
# e = E   1/(n)!
#     n=0 

def calc_e(n):
	total = 1
	for x in range(1, n):
		total = add(total, 1/factorial(x))
	return total

print(calc_e(15))

# Default arguments
def print_thing(thing="thing"):
	print(thing)

print_thing()

'''
Case Study:
Break down a large block of code into smaller more usable blocks

The Code:
We have a list of friend and we want to print out who our best friends are by who has the highest name score.

joshua
j o  s  h u  a
9+14+18+7+20+0 = 68

My opinion of the optimal number of functions to accomplish this goal: 3
'''

def favorite_friends():
	names = ['joshua', 'michael', 'patrick', 'carly', 'brady', 'ethan', 'lexi', 'sage', 'cale', 'ryan', 'josephina', 'dabrazilia']
	for x in range(6):
		bestFriend = ''
		bestScore = 0
		for name in names:
			score = 0
			for letter in name:
				score += ord(letter) % 97
			if score > bestScore:
				bestFriend = name
				bestScore = score
		print("My number", x+1, "pick for a best friend is:", bestFriend, "because they had the highest friend score of", bestScore)
		names.remove(bestFriend)
		bestScore = 0



