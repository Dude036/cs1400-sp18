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
for _ in range(360):
	turtle.forward(35)
	turtle.right(10)
	turtle.pensize(randrange(100))
	turtle.pencolor(randrange(255), randrange(255), randrange(255))

turtle.done()

# Math with dates in datetime - https://docs.python.org/3/library/datetime.html
from datetime import datetime

currentTime = datetime.now()
hour = currentTime.hour

print(hour+9%12, ':', currentTime.minute, ':', currentTime.second)


"""
	Case Study
	- Compute the Distance between two points.with Turtle
"""

import turtle

x1 = int(input("What's the first x Coordinate?: "))
y1 = int(input("What's the first y Coordinate?: "))
x2 = int(input("What's the second x Coordinate?: "))
y2 = int(input("What's the second y Coordinate?: "))

turtle.showturtle()
turtle.pensize(150) # thicc
turtle.penup()
turtle.goto(x1, y1)
turtle.pendown()
turtle.goto(x2, y2)

import math
Distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
print("Distance from the two points:", Distance)

input("Wait")
turtle.done()

