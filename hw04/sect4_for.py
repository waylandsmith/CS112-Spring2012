#!/usr/bin/env python
from hwtools import *

print "Section 4:  For Loops"
print "-----------------------------"

nums = input_nums()

"""

This is all testing code.  Ignore it.
#  count = len(nums)
# print count
# numSum = 0

"""

# 1. What is the sum of all the numbers in nums?

for num in nums:
	num=sum(nums)	# feel like there was a way to do this w/out looking it up, but trial and error didn't work.
	
print "1.", num


# 2. Print every even number in nums


print "2. even numbers"

#CODE GOES HERE


for num in nums:	# goddamnit why did I struggle with this?
	if num % 2 == 0:
		print num

# 3. Does nums only contain even numbers? 
only_even = False

#CODE GOES HERE
oddCount = 0  # Number of odd numbers
for num in nums:
	if num % 2 != 0: # parses for odds
		oddCount += 1
if oddCount == 0:
	only_even = True

# my code ends here
###### 
print "3.",
if only_even:
    print "only even"
else:
    print "some odd"


# 4. Generate a list every odd number less than 100. Hint: use range()
nums2 = []
for num in range(1,100):
	if num % 2 != 0:
		nums2.append(num)

print "4.", nums2

# 5. [ADVANCED]  Multiply each element in nums by its index

#### none of the below works.
# nums3 = []
# for num in nums:
#	num += nums[num]
#	nums3.append(num)
print "5.", __ # nums3
