#!/usr/bin/python


'''
Feb 16 - Exam 1

Review Next week to cover everything. Bring questions
'''
'''
# String concatination
first = "Josh"
last = "Higham"

print(first, last)
print(first + last)
print("$" + str(5.00))

# Boolean Values and how to get them

a = False
print(a)

b = 6 <= 10
print(b)


# Control Block Points
if a:
	print("A is True")
elif b:
	print("B is True")
else:
	print("Both are False")

# Randomness
import random

# randint(<Low Value>, <High Value>) Inclusive
print(random.randint(0, 5))
'''

# # # # # # #  #  # # # # # # # 
# Case Study: The Stupid Tax  #
# # # # # # #  #  # # # # # # #
# Pick two numbers from 0 to 9, and see if you can match them to the slot

in1 = int(input("What's the first guess number?"))
in2 = int(input("What's the second guess number?"))

import random

slot1 = random.randint(0, 9)
slot2 = random.randint(0, 9)
slot3 = random.randint(0, 9)

has1 = False
has2 = False

if in1 == slot1 or in1 == slot2 or in1 == slot3:
	has1 = True
if in2 == slot1 or in2 == slot2 or in2 == slot3:
	has2 = True

if has1 and has2:
	print("You won $10,000!")
elif has1 or has2:
	print("You won $1,000")
else:
	print("You lose.....")

	