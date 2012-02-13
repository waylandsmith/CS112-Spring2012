#!/usr/bin/env python

import random

print "Welcome to the d20 Random Individual Generator v1.1"
# lets_go=raw_input("press any key to generate a random human individual")

al_list=['Lawful Good','Neutral Good','Chaotic Good','Lawful Neutral','True Neutral','Chaotic Neutral','Lawful Evil','Neutral Evil','Chaotic Evil']

# print alignment[alignment]

print al_list[random.randint(0,8)]

### Level

# lvl_list=[

# this is a primitive level generator.  In the long run, weight the level generator.
lvl=random.randint(1,21)

# print "Level",lvl

# this is a primitive class generator.  In the long run, weight this too.
class_list=['Commoner','Warrior','Adept','Aristocrat','Expert','Psion','Soulknife','Psychic Warrior','Wilder','Fighter','Wizard','Rogue','Cleric','Bard','Barbarian','Monk','Druid','Ranger','Sorcerer','Paladin']
chosen_class=class_list[random.randint(0,18)]

print chosen_class,lvl

saves_good=['2','3','3','4','4','5','5','6','6','7','7','8','8','9','9','10','10','11','11','12','12']
saves_bad=['0','0','1','1','1','2','2','2','3','3','3','4','4','4','5','5','5','6','6','6','6']
# B

# BASE ATTACK BONUS

# for class_list[]: BAB=lvl

# if clss_list
