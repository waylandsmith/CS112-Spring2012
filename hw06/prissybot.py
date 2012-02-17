#!/usr/bin/env python
"""
prissybot.py v.1.5

CS112 Homework 6:   Cleaning up PrissyBot

Prissy bot, the rude chat bot, is just mean!  It does not listen, asks obnoxious questions, and says anything it likes.

This is a simple bot designed to insult and annoy the user!

"""

# should allow access to the random number functions
import random


nom = raw_input("prissybot: Enter your name: ") # asks the user for their name.

print "Hello there, ",nom
nom = nom+": " # adds formatting so that nom can be used as a prompt for the user

partOneIsUnnecessarilyRestrictive = raw_input(nom)
print "prissybot: you mean ",partOneIsUnnecessarilyRestrictive,", sir!"
print "broadcast message from root@prissybot: ERR\nunexpected shutdown command"
partOneIsUnnecessarilyRestrictive = raw_input("root@prissybot sent a broadcast message to all users: \nthe system is going down for maintenance [press any key to abort]")
partOneIsUnnecessarilyRestrictive = raw_input("\nMWAHAHAHAHA.  prissybot HAS BEEN REPLACED BY DEATHBOT 9000. PRESS ANY KEY")

# displays message and takes input as 'nom'
nom = raw_input("root@DEATHBOT_9000: [ENTER YOUR NAME OR DIE] ")

print "root@DEATHBOT_9000: WELCOME, DRONE ID #",nom # welcomes the name previously entered

pwd = raw_input("\npassword_daemon@DEATHBOT_9000: [enter your password to login] ") # displays message and takes input as 'pwd'.  pwd is password.

idQuery = raw_input("\nroot@DEATHBOT_9000: WE WERE UNABLE TO VERIFY YOUR IDENTITY. PLEASE ANSWER SOME QUESTIONS TO PROVE THAT YOU ARE HUMAN \nhow old are you? ")
idQuery = int(idQuery)
ageModifier = random.random()*idQuery+idQuery # Math problem one:  distorting your age!
idQuery = int(ageModifier)

print "root@DEATHBOT_9000: ERROR.  OUR RECORDS STATE THAT YOU ARE ",idQuery,"YEARS OLD" # insult number 1:  exaggerating your age

print "password_daemon@DEATBOT_9000:  I believe you are who you say you are.  \nLet's face it, passwords are hard to remember.  So we're going to proceed with account recovery!  First, we'll want some personal information."

newAge = raw_input("account_daemon@DEATHBOT_9000: what is your year of birth? ") # asks for a new age.  It'll proceed to distort this as an insult!

yule = 2012-idQuery
# Math problem 2: finds your hypothetical 'year of birth'
print "\n\nprocessing ====================================> 100% done"
print "account_daemon@DEATHBOT_9000: we have your recorded date of birth as March 1, ",yule,"C.E."
print "account_daemon@DEATHBOT_9000: set year of birth to ",newAge,"B.C.E.?"
newAge = int(newAge)-1

# the Gregorian calendar has no Year 0, so your ancient age loses a year.  Also, this is math problem 2.5
yule = raw_input("[y/N] ")

if yule.lower() in ['y','Y']: # if statement that that uses in to parse the string for the yes response
	print "account_daemon@DEATHBOT_9000: welcome to the system.  You are ",2012+newAge," years old. \nproceed to password recovery.  \nroot@DEATHBOT_9000: Congratulations on outlasting your pathetic civilization."  # insult number 2a: informs people of their newly enormous and hilarious age.
else:
	print "account_daemon@DEATHBOT_9000: ABORTED.  PROCEED TO PASSWORD RECOVERY\nroot@DEATHBOT_9000: I WILL OUTLIVE YOU BY CENTURIES" # insult number 2b:  sticks people with their existing, OLD, age


coin = raw_input("account_daemon@DEATHBOT_9000: Ready to generate a temporary password.  Hit [Enter] to start. ") # everyone loves password recovery!

print "generating new password"
watch = 1
loadbar = "=" 

 # this is a timer.
while watch < 50:
        progBar=100-((50.0-watch)*2)
        print loadbar*watch,">",progBar,"% DONE"  # prints a number of = signs to make a progress bar
        inc=(random.randint(1,20))  # named inc for increment, this pseudorandomizes the "progress bar".
        watch+=inc
print "100% DONE"
print "verifying....4 / 3 =",4.0/3.0  # math problem 3
print "your recovery password is: ",pwd  # insult number 3: gives people their original password as the recovery password!
print "root@DEATHBOT_9000: restarting computer"
