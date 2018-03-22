#!/usr/bin/python3

'''
	Classes

'''

class Fish(object):
	"""docstring for Fish"""
	__scales = 0
	colorOfScales = ''
	hunger = 0

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

	# This is a getter function. It simply retrieves information (most often private)
	def look(self):
		return self.colorOfScales




