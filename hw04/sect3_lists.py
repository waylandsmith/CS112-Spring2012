#!/usr/bin/env python
from hwtools import *

print "Section 3:  Lists"
print "-----------------------------"

print "root@DEATHBOT_9000 says:  YOU MUST GIVE MORE THAN THREE NUMBERS FOR THIS PROGRAM TO WORK"

nums = input_nums()
# 1. "nums" is a list of numbers entered from the command line.  How many
#    numbers were entered?


thisWasWayHarderInMyHead=len(nums)

print "1.",thisWasWayHarderInMyHead


# 2.  Append 3 and 5 to nums

nums.append(3)
nums.append(5)

print "2.", nums

# 3.  Remove the last element from nums

countingNums = thisWasWayHarderInMyHead-1
countingNums = int(countingNums)

# print countingNums  # makes sure that countingNums works for TESTING PURPOSES

# [:countingNums] tells the list to end at countingNums
nums=nums[:countingNums]

print "3.", nums


# 4.  Set the 3rd element to 7

nums[2]=7

#nums2=nums[2:2]
#nums[2]='7'
#nums=nums2[:]

print "4.", nums


# 5. [ADVANCED] Grab a new list of numbers and add it to the existing one

# print "5.", nums


# 6. [ADVANCED] Make a copy of this new giant list and delete the 2nd 
#    through 4th values

# nums_copy = __
# print "6.", nums, nums_copy

# 7-9. [ADVANCED] Print the following:

# print "7.", nums[__]    # first 3 elements
# print "8.", nums[__]    # last element
# print "9.", nums[__]    # a list of the second element
