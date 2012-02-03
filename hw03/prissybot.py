#!/usr/bin/env python
"""
prissybot.py

CS112 Homework 3:   PrissyBot

Prissy bot, the rude chat bot, is just mean!  It does not listen, asks obnoxious questions, and says anything it likes.
"""

# Step 1:
# -----------------------
# Program the following.
# 
#    $ python prissybot.py
#    Enter your name:  Paul
#   
#    PrissyBot: Hello there, Paul
#    Paul: hi bot
#    PrissyBot: You mean, "hi bot, sir!"
# 
# Make sure the user inputs their own name and responses.

# Step 2:
# -----------------------
# Keep adding to the conversation. Make sure that your program 
# includes the following:
# 
#  * get and use input from the user
#  * 3 math problems
#     * at least one should get numbers from the user
#  * at least 3 insults


# Advanced
# -------------------------
# Make sure your prissy bot uses string formatting throughout.  
# Also, create new programs for the following:
#  
#  1. draw some kind of ascii art based on user input
#  2. print a decimal/binary/hexidecimal conversion table 
#     * well formated and labeled
#     * reads 5 numbers from the input (all less than 256)
#  3. reduce a fraction
#     * read a numerator and denominator from the user
#     * ex.  6/4 = 1 2/4

import random
# should allow access to the random number functions
# thank you docs.python.org ^^

nom=raw_input("prissybot: Enter your name: ")
print "Hello there, ",nom
nom=nom+": "
partOneIsUnnecessarilyRestrictive=raw_input(nom)
print "prissybot: you mean ",partOneIsUnnecessarilyRestrictive,", sir!"
print "broadcast message from root@prissybot: ERR\nunexpected shutdown command"
partOneIsUnnecessarilyRestrictive=raw_input("root@prissybot sent a broadcast message to all users: \nthe system is going down for maintenance [press any key to abort]")
partOneIsUnnecessarilyRestrictive=raw_input("\nMWAHAHAHAHA.  prissybot HAS BEEN REPLACED BY DEATHBOT 9000. PRESS ANY KEY")
# if you think this is back, imagine.  I considered having yout hit enter for every single line of output.
# every one.  


nom=raw_input("root@DEATHBOT_9000: [ENTER YOUR NAME OR DIE] ")
# displays message and takes input as 'nom'

print "root@DEATHBOT_9000: WELCOME, DRONE ID #",nom
# welcomes the name previously entered

pwd=raw_input("\npassword_daemon@DEATHBOT_9000: [enter your password to login] ")
# displays message and takes input as 'pwd'.  pwd is password.


captcha=raw_input("\nroot@DEATHBOT_9000: WE WERE UNABLE TO VERIFY YOUR IDENTITY. PLEASE ANSWER SOME QUESTIONS TO PROVE THAT YOU ARE HUMAN \nhow old are you? ")

captcha=int(captcha)
ageModifier=random.random()*captcha+captcha
# Math problem one:  distorting your age!
captcha=int(ageModifier)
# a deadly, deadly captcha.

print "root@DEATHBOT_9000: ERROR.  OUR RECORDS STATE THAT YOU ARE ",captcha,"YEARS OLD"
# insult number 1:  exaggerating your age
print "password_daemon@DEATBOT_9000:  I believe you are who you say you are.  \nLet's face it, passwords are hard to remember.  So we're going to proceed with account recovery!  First, we'll want some personal information."
newAge=raw_input("account_daemon@DEATHBOT_9000: what is your year of birth? ")
# asks for a new age.  It'll proceed to distort this for crazy hijinks!

yule=2012-captcha
# Math problem 2: finds your hypothetical 'year of birth'
print "\n\nprocessing ====================================> 100% done"
print "account_daemon@DEATHBOT_9000: we have your recorded date of birth as March 1, ",yule,"C.E."
print "account_daemon@DEATHBOT_9000: set year of birth to ",newAge,"B.C.E.?"
newAge=int(newAge)-1
# the Gregorian calendar has no Year 0, so your ancient age loses a year.  Also, this is math problem 2.5
yule=raw_input("[y/N] ")
if yule.lower() in ['y','Y']: 
# I had to look up how to make this work.  Earlier versions had the URL of the tip (someone else's problem) that helped me figure it out, but for some reason even in comment form the URL broke the interpreter.  Suffice to say that I couldn't get it to work, looked up the problem, and found out about both the 'in' thing and how to get stuff from the strings module.  
# if statement that that uses in to parse the string for the yes response
	print "account_daemon@DEATHBOT_9000: welcome to the system.  You are ",2012+newAge," years old. \nproceed to password recovery.  \nroot@DEATHBOT_9000: Congratulations on outlasting your pathetic civilization."
# insult number 2a: informs people of their newly enormous and hilarious age.
else:
	print "account_daemon@DEATHBOT_9000: ABORTED.  PROCEED TO PASSWORD RECOVERY\nroot@DEATHBOT_9000: I WILL OUTLIVE YOU BY CENTURIES"
# everyone loves password recovery!
# insult number 2b:  sticks people with their existing, OLD, age

coin=raw_input("account_daemon@DEATHBOT_9000: Ready to generate a temporary password.  Hit [Enter] to start. ")
# because arcade games use coins to continue

print "generating new password"
watch=1
loadbar= "="
# this is a timer.  Wish I knew how to make it real-time.
while watch < 50:
        progBar=100-((50.0-watch)*2)
        print loadbar*watch,">",progBar,"% DONE"
        # prints a number of = signs to make a progress bar
        inc=(random.randint(1,20))
        # named inc for increment, this pseudorandomizes the "progress bar".
        watch+=inc
print "100% DONE"
print "verifying....4 / 3 =",4.0/3.0
# math problem 3
print "your recovery password is: ",pwd
# insult number 3: gives people their original password as the recovery password!
print "root@DEATHBOT_9000: restarting computer"
