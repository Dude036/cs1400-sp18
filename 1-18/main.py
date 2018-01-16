#!/usr/bin/python

"""
Demonstration for Sections 2.1 to 2.7

2.1 Introduction 32

2.2 Writing a Simple Program 32

2.3 Reading Input from the Console 34

2.4 Identifiers 36

2.5 Variables, Assignment Statements, and Expressions 36

2.6 Simultaneous Assignments 38

2.7 Named Constants 39

"""

# 2.2 Simple Program
farenheit = 32
celcius = (farenheit - 32) * 5/9

print(farenheit, "degrees Farenheit is", celcius, "degrees Celcius")


# 2.3 Reading input from the console
variable = int(input("Enter a degree in Farenheit: "))
celcius = (variable - 32) * 5/9

print(variable, "degrees Farenheit is", celcius, "degrees Celcius")


# 2.5 Variables, Assignment, and Expressions
x = 1
do_a_thing = 5

# 2.6 Simultaneous Assignment
c = 15
a = 10
b = 5

print("A = ", a)
print("B = ", b)

a, b = b, a

print("A = ", a)
print("B = ", b)

a = b = c = 20

print("A = ", a)
print("B = ", b)
print("C = ", c)


# 2.7 Constants

CONSTANT = 42
constant = 0

print(CONSTANT)
