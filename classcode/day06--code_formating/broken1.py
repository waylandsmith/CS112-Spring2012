#!/usr/bin/env python

### THIS WAS AN EXCERSIZE IN PROPER FORMATTING

input_list=[]
input_number=None

# get list of numbers from the user
while input_number != "":
	input_number=raw_input()
	if input_number.isdigit():
		input_list.append(float(input_number))

# get list of numbers from user.
total=0
for num in input_list:  # we declae the variable, 'num', in the for loop itself!
    total += num

# print average of list
print total/len(input_list)
