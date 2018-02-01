#!/usr/bin/python

'''
Case Studies will be homework assignments from now on


'''


# Using Turtle - https://docs.python.org/3.3/library/turtle.html
import turtle
from random import randrange

# turtle.circle(50)

turtle.colormode(255)
turtle.penup()
turtle.goto(0, 150)
turtle.pensize(12)
turtle.pendown()
# Ignore this line	
for _ in range(36):
	turtle.forward(35)
	turtle.right(10)
	turtle.pencolor(randrange(255), randrange(255), randrange(255))

turtle.done()
'''

# Math with dates in datetime - https://docs.python.org/3/library/datetime.html
from datetime import datetime

currentTime = datetime.now()
hour = currentTime.hour

print(hour%12, ':', currentTime.minute, ':', currentTime.second)

'''
"""
	Case Study
	- Compute the Distance between two points.with Turtle
"""


