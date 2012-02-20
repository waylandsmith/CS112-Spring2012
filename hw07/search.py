#!/usr/bin/env python
"""
Binary Search

This was supposed to be a binary search algorithm but it isn't working...
I used the Iterative implementation from here:
    http://en.wikipedia.org/wiki/Binary_search_algorithm
"""
from hwtools import input_nums

nums = input_nums()
sorted(nums)

print "I have sorted your numbers"

numSeek = raw_input("Which number should I find: ")
numSeek = int(numSeek)
mid = 1
listLength = len(nums)-1 # gets the length the length of the list

while listLength >= mid:
    midPoint = listLength + (mid / 2) # searches for the middle value continously

    if nums[midPoint] == numSeek:
        break # ends the loop if the middle value is the value searched for
    elif numSeek > nums[midPoint]: # if the search is greater than the middle,
        mid = midPoint + 1 # search a higher group
    else:
        listLength -= 1 # search a lower group

if nums[midPoint] == numSeek: # successful find message
    print "Found", numSeek , "at", midPoint
else:
    print "Could not find", numSeek
