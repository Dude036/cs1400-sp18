#!/usr/bin/python3

# Using Lists with Functions
name = 'Josh Higham'

for l in range(len(name)):
	print(name[l], end='')
print()

for l in name:
	print(l, end='')
print()


def capitals(name):
	count = 0
	for l in name:
		if l.isupper():
			count += 1
	return count


print("There are " + str(capitals(name)) + " capital letters in", name)

# Sorting lists
import random
nums = [i for i in range(20)]

print(nums)
random.shuffle(nums)

print(nums)
nums.sort(reverse=True)

print(nums)


'''
This was supposed to be your case study, but It didn't demonstrate what I wanted it to. 
Counting the occurance of letters in a string
'''

def occurance(s):
	alphabet = []
	for letter in range(25):
		alphabet.append(s.count(chr(ord('a') + letter)) + s.count(chr(ord('A') + letter)))
	return alphabet

print(occurance('A quick brown fox jumps over the lazy dog'))


'''
Case Study: Count the occurance of unique letters in a string
'''



