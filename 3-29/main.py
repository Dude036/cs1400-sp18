#/bin/usr/python


'''
Exam #2 - Review Session

'''

# Range with 3 inputs
for x in range(10, 1, -2):
	print(x)


print(id(3))


g1 = "Good"
g2 = "Good"
print(id(g1), id(g2))
g2 = "Bad"
print(id(g1), id(g2))
print(g2.replace('B', 'S', 1))


def f(a, b, c, d, e=5):
	print(a,b,c,d,e)

f(1, 2, 3, 4)
# Wrong: Positional arguments after Keyword Arguments 
# f(a=1, 2, 3, 4)
# f(2, 3, 4,a=1)
# f(a=1, b=2, 3, 4)
f(a=1, b=2, c=3, d=4)
f(1, 2, 3, d=4)


print('programming is fun'.replace('m', 't'))
print('programming is fun'[0:-3])
print('programming is fun'.startswith('pro'))
print('programming is fun'[3:])
print('programming is fun'[0:4])
print('programming is fun'[:3])
print('programming is fun'[:2])


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


class PlayingCard(object):
	suit = ''
	value = 0
	"""docstring for PlayingCard"""
	def __init__(self, Suit, Num):
		self.suit = Suit
		self.value = Num

	def get_value(self):
		return self.value
	
	def get_suit(self):
		return self.suit

	def get_card(self):
		return self.suit, self.value

	def get_id(self):
		return id(self)


card = PlayingCard('Spade', 2)

print(card.get_card())
print(PlayingCard.get_value(card))
