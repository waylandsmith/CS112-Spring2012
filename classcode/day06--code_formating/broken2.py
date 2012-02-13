#!/usr/bin/env python
from random import randint


inputNumber=int(raw_input())
numberList=[]

# this section creates a series of random numbers in numberList equal to the length of the input
for nameless in range(inputNumber):
    numberList.append(randint(0,20))
print numberList

"""
notDone=1
while notdone:
    notDone=0 # the loop will only loop once

    for var in range(1,inputNumber):
        if numberList[var-1] > numberList[var]:
            t1= numberList[var-1]
            t2= numberList[var]
            numberList[var-1] = t2
            numberList[var] = t1
            s=1
print numberList
"""
