#!/usr/bin/python3
	
'''
	Classes

'''

class Fish(object):
	"""docstring for Fish"""
	__scales = 0
	colorOfScales = ''
	hunger = 0
	children = 0

	def __init__(self, newScales, newColor='Yellow'):
		self.__scales = newScales
		self.colorOfScales = newColor

	def swim(self):
		print("The fish is swimming.")

	def eat(self, amount):
		self.hunger += amount
		if self.hunger > 100:
			print("Your fish is very full.")
		elif self.hunger < 10:
			print("Your fish is very hungry still.")

	# This is a setter function. It changes stuff that's private
	def mature(self, scaleRate):
		self.__scales *= scaleRate
		print("Our fishy friend has grown up!")
		print("He now has", self.__scales, "scales!")
		
	def getChildren(self):
		return self.children

	def setChildren(self, newKid):
		if newKid < 0:
			print("You can't have negative children!")
			newKid = 0
		self.children = newKid

	def __function(self):
		print("This is a hidden function")

	# This is a getter function. It simply retrieves information (most often private)
	def look(self):
		return self.colorOfScales

Nemo = Fish(500, 'Orange')

print(Nemo.colorOfScales)

Nemo.eat(500)

Nemo.mature(5)

print(Nemo.getChildren())
Nemo.setChildren(-2)
print(Nemo.getChildren())





# import time

# t1 = time.time()

# t2 = time.time()

# t3 = t1 - t2


