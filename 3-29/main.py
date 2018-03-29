#/bin/usr/python


'''
Exam #2 - Review Session

'''

# Range with 3 inputs
for x in range(1,10):
	print(x)





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
