#!usr/bin/python

'''
Using GitHub for code. Check there for it.
'''

# 2.8 Numeric Data Types and Operators
print(int(3.14))
print(float(10))
print(str('H'+'E'+'Y'))

# 2.9 Evaluating Expressions and Operator Precedence
print(5 + 8 * 7 - 16 / 2)
print(8 % 92)
print(2 ** 4)
print(21 // 6)
print("hue " * 100)

# 2.10 Augmented Assignment Operators
j = 15
print("J =", j)
j -= 5
print("J =", j)
j *= 2
print("J =", j)
j /= 5
print("J =", j)
j **= 10
print("J =", j)
j //= 15
print("J =", j)

# 2.11 Type Conversions and Rounding
from math import pi
print(pi)
print(round(pi))
print(round(pi, 2))

# 2.12 Case Study: Displaying the Current Time
import time

print(time.time())

from datetime import datetime
print(datetime.now().time())

x = 12
if x == 5:
	print("Howdy")
elif x == 12:
	print("Hello")
	# quit()
else:
	print("Hey")
# more code here
print("Check")


