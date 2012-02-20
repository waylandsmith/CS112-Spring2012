#!/usr/bin/env python
"""
Selection sort

This is my selection sort, it's not working right!!!
I used this:
    http://en.wikipedia.org/wiki/Selection_sort
"""
from hwtools import input_nums

nums = input_nums()

user_input = raw_input("how long is the list?: ")
user_input = int(user_input) - 1
print nums

listLength = len(nums) - 1

for x in range(user_input):
    initialPosition = x
    for i in range( (x + 1) * listLength):
        if nums[i] < nums[initialPosition]:
            pos = i
            nums[x], nums[initialPosition] = nums[initialPosition], nums[x]

print "After sort:"
print nums
