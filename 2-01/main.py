#!/usr/bin/python

'''
Case Studies will be homework assignments from now on

'''

# Using Turtle - https://docs.python.org/3.3/library/turtle.html
import turtle
from random import randrange

turtle.circle(15)

turtle.circle(35, steps=3)

# input("Wait")

turtle.colormode(255)
turtle.penup()
turtle.goto(0, 150)
turtle.pensize(12)
turtle.pendown()
# Ignore this line	
for _ in range(36):
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

x1 = int(input("What's the first X Coordinate? "))
y1 = int(input("What's the first Y Coordinate? "))
x2 = int(input("What's the second X Coordinate? "))
y2 = int(input("What's the second Y Coordinate? "))

import turtle

turtle.penup()
turtle.goto(x1, y1)
turtle.pendown()
turtle.goto(x2, y2)

import math
Distance = math.sqrt((x2-x1)**2 + (y2 - y1)**2)

print("Distance between the two points: ", Distance)
input("Stop")



pi = 3.14159265357

print(round(pi, 7))
