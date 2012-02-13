#!/usr/bin/env python
from hwtools import *

print "Section 2:  Loops"
print "-----------------------------"

# 1. Keep getting a number from the input (num) until it is a multiple of 3.
num = 0
while num == 0:
	bun = raw_input("Please give me a multiple of 3: ")
	bun = int(bun)
	if (bun/3)==(bun/3.0):
		num = bun
	else:
		print "That wasn't an even multiple of 3, jerk!"

print "1.", num

# 2. Countdown from the given number to 0 by threes. 
#    Example:
#      12...
#      9...
#      6...
#      3...
#      0

# Wish I coulda made it pretty.  There were several versions.
num = [num]
done = True
while bun != 0:
	bun-=3
	num+=[bun]


print "2. Countdown from", num

#CODE GOES HERe
# 3. [ADVANCED] Get another num.  If num is a multiple of 3, countdown 
#    by threes.  If it is not a multiple of 3 but is even, countdown by 
#    twos.  Otherwise, just countdown by ones.

# num = int(raw_input("3. Countdown from: "))

countdown = 0
num2 = [0]
bun = raw_input("root@DEATHBOT_9000 sent out a broadcast message:  ENTER A NUMBER OF DIE: ")
bun = int(bun)
if (bun/3) == (bun/3.0):
	num2[0] = bun
#	countdown = bun
	while bun != 0:
		bun-=3
		num2+=[bun]
else:
	if (bun/2)==(bun/2.0):
		num2[0] = bun
		while bun != 0:
			bun-=2
			num2+=[bun]
	else:
		num2[0] = bun
		while bun != 0:
			bun-=1
			num2+=[bun]

print num2

# thought:  I should come back to this later and figure out how to get it to print out a new line per item.
