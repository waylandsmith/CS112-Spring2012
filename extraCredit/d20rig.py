#!/usr/bin/env python

import random
import csv

"""
# generic example below
# format = [hit die,fort save,reflex save,will save,base attack bonus,skill points,is_caster]
# example = [d4,poor,poor,poor,poor,2,FALSE]
example_class = csv.reader(open("d20ruleset.csv", "rb"))

for row in example_class:
    print row
"""

# for class_list[]: BAB=lvl

# if clss_list

print "Welcome to the d20 Random Individual Generator v1.4" # version 1.0 having been my JavaScript version @ the end of Web Design.
# version 1.3 released on February 15, 2012
# version 1.4.5 alpha finished on February 20, 2012
# release notes:  added CSV support and health point generation for all classes.  Added Saving Throws (experimental) and some attack bonuses.

# lets_go=raw_input("press any key to generate a random human individual")

al_list = ['Lawful Good','Neutral Good','Chaotic Good','Lawful Neutral','True Neutral','Chaotic Neutral','Lawful Evil','Neutral Evil','Chaotic Evil']

# print alignment[alignment]

print al_list[random.randint(0,8)]

### Level

# this is a primitive level generator.  In the long run, I'll need to weight the level generator to favor the first few levels.
# level range as a module is also a possibility, but not really something I intend to invoke initially
lvl = random.randint(1,21)

# print "Level",lvl

# this is a primitive class generator.  In the long run, weight this too.
class_list = ['Commoner','Warrior','Adept','Aristocrat','Expert','Psion','Soulknife','Psychic Warrior','Wilder','Fighter','Wizard','Rogue','Cleric','Bard','Barbarian','Monk','Druid','Ranger','Sorcerer','Paladin']

chosen_class = class_list[random.randint(0,18)]
# chosen_class = "Commoner"

print chosen_class,lvl

# ABILITIES

# generic function:
# random.randint(1,6) + random.randint(1,6) + random.randint(1,6)
# rolls three six-sided die.  Sort of.

"""
Features that need to be added:

> a way to inflate the scores that does not derive from the D&D 3.5 DMG but produces a number closer to traditional Dungeons and Dragons (TM Wizards of the Coast) score generation
> a way to make sure that the ability scores do not conflict with class....IE, a Wizard capable of casting level 3 spells should not be generated with Intelligence < 13
> a module to choose character ability methods.  If this functionality could be added, the user could specify to use certain scores or certain ranges

"""

# abilities are generated seperately from the print statement so that the program can reference them later.
strength = random.randint(1,6) + random.randint(1,6) + random.randint(1,6) 
dexterity = random.randint(1,6) + random.randint(1,6) + random.randint(1,6)
constitution = random.randint(1,6) + random.randint(1,6) + random.randint(1,6)
intelligence = random.randint(1,6) + random.randint(1,6) + random.randint(1,6)
wisdom = random.randint(1,6) + random.randint(1,6) + random.randint(1,6)
charisma = random.randint(1,6) + random.randint(1,6) + random.randint(1,6)

str_mod = (strength - 10) / 2
dex_mod = (dexterity - 10) / 2
con_mod = (constitution - 10) / 2
int_mod = (intelligence - 10) / 2
wis_mod = (wisdom - 10) / 2
cha_mod = (charisma - 10) / 2

# prints out the abiilities
print "Strengh:",strength,"Dexterity:",dexterity,"Constitution:",constitution,"Intelligence:",intelligence,"Wisdom:",wisdom,"Charisma:",charisma
print str_mod,dex_mod,con_mod,int_mod,wis_mod,cha_mod

# score_bonus = (<score> - 10) / 2 # the bonus from an ability score

# SAVING THROWS

# this list contains the progression for saving throws based on level
saves_good = ['2','3','3','4','4','5','5','6','6','7','7','8','8','9','9','10','10','11','11','12','12']
saves_bad = ['0','0','1','1','1','2','2','2','3','3','3','4','4','4','5','5','5','6','6','6','6']


# BASE ATTACK BONUS
BAB_good = lvl
BAB_average = ['0','1']	# god I hate medium BAB classes.
BAB_poor = lvl / 2	# I love that by doing Int math, we auto-round-down just as d20 rules demand.  Yay laziness!

# SKILLS

# HIT DIE
d4 = (2 * lvl)
d6 = (3 * lvl)
d8 = (4 * lvl)
d10 = (5 * lvl)
d12 = (6 * lvl)

# CLASS INFO

# generic example below
# format = [hit die,fort save,reflex save,will save,base attack bonus,skill points,is_caster]
# example = [d4,poor,poor,poor,poor,2,FALSE]

example_class = csv.reader(open("d20classes.csv", "rb")) # READS FROM THE csv FILE

# THE STATS WE'LL BE CRUNCHING
bab = 0
fort = 0
reflex = 0
wills = 0
hd = 0

##############
# MAIN LOOP
##############

for row in example_class:
#    filter(class_parser, example_class) # took me a while to figure out how to manipulate objects from the CSV
    if row[0] in chosen_class:
        hd = ((int(row[1]) / 2) * lvl) + (con_mod * lvl)
        print "Health:",hd,"hit points"
        if row[2] in 'GOOD':
            fort = saves_good[lvl-1]
            fort = int(fort) + con_mod
        else:
            fort = saves_bad[lvl-1]
            fort = int(fort) + con_mod
        print "Fortitude save =",fort
        if row[3] in 'GOOD':
            reflex = saves_good[lvl-1]
            reflex = int(reflex) + dex_mod            
        else:
            reflex = saves_bad[lvl-1]
            reflex = int(reflex) + dex_mod            
        print "Rexlex Save =",reflex
        if row[4] in 'GOOD':
            wills = saves_good[lvl-1]
            wills = int(wills) + wis_mod            
        else:
            reflex = saves_bad[lvl-1]
            reflex = int(wills) + wis_mod            
        print "Will Save =",wills
        if row[5] in 'GOOD':
            bab = BAB_good
        elif row[5] in 'POOR':
            bab = BAB_poor
        else:
            break

print "Base Attack Bonus =",bab







#####################################
# THIS IS ALL JUNK
#####################################
#    else:
#        print "to be added"



#    row = str(row
#    if row.lower() in ['commoner']:
#        print row
#if chosen_class is "Commoner":
#    print example_class.next()
#    print example_class.next()
#    for row in ("Commoner" in example_class.next()):
#        print row
#        class_row = csvreader.next(example_class)
#        print row
#    hd = d4 # next step:  find a way to access a specific row or position
#else:
#    print "details to come"
 
# hip = hd + (constitution * lvl) # a character's hit point total

# print "Health",hd,"Hit Points"

# for class_list[]: BAB=lvl

# if clss_list
