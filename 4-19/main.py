#!/usr/bin/python3

# Two dimensional lists and their traversal


def twoDList():
	import random
	l = []
	for _ in range(10):
		templ = []
		for _ in range(10):
			templ.append(random.randint(0, 10))
		l.append(templ)
	print(l)
	for x in l:
		print(x)
		for y in x:
			print(y)
	return l

# twoDList()
