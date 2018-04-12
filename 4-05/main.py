'''
HW10 - Stuff you may want to know

__cmp__ - Compare
__lt__  - Less than
__le__  - Less than or equals
__eq__  - Equals
__ne__  - Not equals
__gt__  - Greater than
__ge__  - Greater than or equals

'''

from enum import Enum

class Suit(Enum):
	SPADE = 1
	HEART = 2
	CLUB = 3
	DIAMOND = 4


class PlayingCard(object):
	suit = Suit.SPADE
	value = 0
	"""docstring for PlayingCard"""
	def __init__(self, Suit, Num):
		self.suit = Suit
		self.value = Num

	def get_value(self):
		return self.value
	
	def get_suit(self):
		return self.suit

	def __cmp__(self, other):
		pass

	def __lt__(self, other):
		pass

	def __le__(self, other):
		pass

	def __eq__(self, other):
		return self.value == other.value and self.suit == other.suit
			
	def __ne__(self, other):
		return self.value != other.value and self.suit != other.suit

	def __gt__(self, other):
		# print(self.suit)
		# if self.value > other.value:
		# 	return True
		# elif self.value == other.value:
		# 	return self.suit < other.suit
		pass

	def __ge__(self, other):
		pass


c9 = PlayingCard(Suit.CLUB, 9)
c = PlayingCard(Suit.CLUB, 9)
sa = PlayingCard(Suit.SPADE, 14)
c8 = PlayingCard(Suit.CLUB, 8)

print(c8.__eq__(c9))
print(c8 == c9)

# print()

'''
Lists and Tuples - How do they work

'''

l = [1, 2, 3, 4, 5]
t = (1, 2, 3, 4, 5)

for c in t:
	print(c)

l[1] = 15
# t[1] = 15 Bad idea

def function():
	return 1, 2, 3

print(function())



li = []

for x in range(1,15):
	li.append(x)

print(li)

import pprint

pp = pprint.PrettyPrinter(indent = 2)

twoD = []

for x in range(1, 10):
	v = []
	for y in range(1, x+3):
		v.append(y*x)
	twoD.append(tuple(v))
	v.clear()
	pp.pprint(twoD)


# print(twoD[4][8])


