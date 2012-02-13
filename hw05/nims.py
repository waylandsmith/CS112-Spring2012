#!/usr/bin/env python


"""
nims.py

A simple competitive game where players take stones from stone piles.
"""


pile = raw_input("How many stones are in the pile? ")
pile = int(pile)
# by setting the limiter here we can change it in one place if we want to.
limiter=5
print "the number of stones in the pile: ",pile
print "you may take stones from the pile less than or equal to",limiter,"each round"

msg = " stones left. Player One: "
altMsg = " stones left.  Player Two: "

# testing code from me trying to have a decent format for the output.   Didn't work.
#msg=str(msg)
#print msg


# the below is testing code.  I wanted to fix the (pile,'msg') output and couldn't find the way, which I'm sure
# is incredibly simple and easy, which only adds to my frustration and rage. RAAAAAAAAAAAAAGE.
# print pileMessage

### GAME LOOP

# why the hell can't I get a way of asking people for input using existing variables WITHOUT those godawful goddamn quotes?
# take=raw_input(pile," stones left  Player 1, take stones")


count = 2	         # keeps track of whose turn it is


# the main event.  Or is it main()? ;)

while pile > 0:
	if count / 2.0 == count / 2:
		pileMessage=str(pile)+msg
	else:
		pileMessage= str(pile)+altMsg
	take = raw_input(pileMessage)
	take= int(take)
	if take > limiter:
		print "invalid number!"
	elif take > pile:
		print "not enough stones"
	elif take < 0:
		print "ERROR.  DEATHBOT DOES NOT UNDERSTAND YOUR NEGATIVE NUMBERS"
	else:
		pile-= take
		count+= 1

if count / 2.0 == count / 2:
	print "player one wins!"
else:
	print "player two wins!"
