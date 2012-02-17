#!/usr/bin/env python


"""
nims.py v. 2:  better formatting and new functionality.

A simple competitive game where players take stones from stone piles.
"""


pile = raw_input("How many stones are in the pile? ")
pile = int(pile)

limiter=5 # by setting the limiter here we can change it in one place if we want to.

print "the number of stones in the pile: ",pile
print "you may take stones from the pile less than or equal to",limiter,"each round"

msg = " stones left. Player One: "
altMsg = " stones left.  Player Two: "


### GAME LOOP

count = 2	         # keeps track of whose turn it is

# the main event.  Or is it main()? ;)

while pile > 0:

# first if statement keeps track of whose turn it is.
	if count / 2.0 == count / 2:
		pileMessage = str(pile)+msg
	else:
		pileMessage = str(pile)+altMsg

# gets the user's input
	take = raw_input(pileMessage)
	take = int(take)

# works with the user's input
	if take > limiter:  # prevents taking too many stones!
		print "invalid number!"
	elif take > pile:
		print "not enough stones"
	elif take == 0:
		print "root@DEATHBOT_9000 says:  enter an interger greater than or equal to 1"  # changelog:  this is a new feature to v.2.  Previous versions accepted a 0 entry.
	elif take < 0:
		print "ERROR.  DEATHBOT DOES NOT UNDERSTAND YOUR NEGATIVE NUMBERS"
	else: # this is the key statement in the input loop.
		pile -= take # takes from the pile
		count += 1 # changes the turn

# declares the winner
if count / 2.0 == count / 2:
	print "player one wins!"
else:
	print "player two wins!"
