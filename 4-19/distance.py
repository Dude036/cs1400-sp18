#!/usr/bin/python3

import math

def writeRandomXY():
	''' This is for your use if you want. It may or may not be useful to you in the future '''
	import random
	with open('distances.txt', 'w') as outf:
		for _ in range(100):
			outf.write(str(random.randint(-10, 9) + random.random()) + ' ')
			outf.write(str(random.randint(-10, 9) + random.random()) + '\n')


def readFile():
	''' This is for your use if you want. It may or may not be useful to you in the future '''
	l = []
	with open('distances.txt', 'r') as inf:
		contents = inf.readlines()
	import re
	for x in contents:
		m = re.match(r'([-]?\w\.[\w]+) ([-]?\w\.[\w]+)', x)
		l.append([float(m.group(1)), float(m.group(2))])

	return l


def distance(x1, y1, x2, y2):
	pass


def findClosestPair(xypair):
	pass

if __name__ == '__main__':
	xypair = readFile()
	

	