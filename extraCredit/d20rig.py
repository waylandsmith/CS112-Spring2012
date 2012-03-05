#!/usr/bin/env python

import random
import csv

print "Welcome to the d20 Random Individual Generator v1.5" # version 1.0 having been my JavaScript version @ the end of Web Design.
# version 1.3 released on February 15, 2012
# version 1.4.5 alpha finished on February 20, 2012
# version 1.5 alpha finished on February 21, 2012
# current version notes: now full support for a CSV sheet which details HD, BAB, Saves, Skill Points, and True/False caster status.


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

> a native, OGL-friendly score generation that doesn't give underpowered scores.  Score modules would go well, too.
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

# print str_mod,dex_mod,con_mod,int_mod,wis_mod,cha_mod

# score_bonus = (<score> - 10) / 2 # the bonus from an ability score

# SAVING THROWS

# this list contains the progression for saving throws based on level
saves_good = ['2','3','3','4','4','5','5','6','6','7','7','8','8','9','9','10','10','11','11','12','12']
saves_bad = ['0','0','1','1','1','2','2','2','3','3','3','4','4','4','5','5','5','6','6','6','6']


# BASE ATTACK BONUS
BAB_good = lvl
BAB_avg = ['0','1','2','3','3','4','5','6','6','7','8','9','9','10','11','12','12','13','14','15','15']	# god I hate medium BAB classes.
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
sp = 2
hd = 0
cl = 0

##############
# MAIN LOOP
##############

for row in example_class:
#    filter(class_parser, example_class) # took me a while to figure out how to manipulate objects from the CSV
    if row[0] in chosen_class:
        hd = ((int(row[1]) / 2) * lvl) + (con_mod * lvl)

        if row[2] in 'GOOD':
            fort = saves_good[lvl-1]
            fort = int(fort) + con_mod
        else:
            fort = saves_bad[lvl-1]
            fort = int(fort) + con_mod

        if row[3] in 'GOOD':
            reflex = saves_good[lvl-1]
            reflex = int(reflex) + dex_mod            
        else:
            reflex = saves_bad[lvl-1]
            reflex = int(reflex) + dex_mod            

        if row[4] in 'GOOD':
            wills = saves_good[lvl-1]
            wills = int(wills) + wis_mod            
        else:
            wills = saves_bad[lvl-1]
            wills = int(wills) + wis_mod            

        if row[5] in 'GOOD':
            bab = BAB_good
        elif row[5] in 'POOR':
            bab = BAB_poor
        else:
            bab = BAB_avg[lvl-1]

        sp = ((int(row[6])) + int_mod) * lvl
        
        if row[7] in 'TRUE':
            cl = lvl
        else:
            break


print "Health:",hd,"hit points"
print "Base Attack Bonus =",bab
print "Fortitude save =",fort
print "Rexlex Save =",reflex
print "Will Save =",wills
print sp,"Skill Points"
if cl > 0:
    print "Caster Level",cl
