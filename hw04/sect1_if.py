#!/usr/bin/env python
from hwtools import *

print "Section 1:  If Statements"
print "-----------------------------"

# 1.  Is n even or odd?
n = raw_input("Enter a number: ")
n = int(n)

n_backup = int(n)
glados = "even"
if (n/2.0)==(n/2):
	glados = "even"
else:
	glados = "odd"
	n_backup*=2

print "1.", glados


# 2. If n is odd, double it
print "2.", n_backup



# 3. If n is evenly divisible by 3, add four
if (n/3.0)==(n/3):
	n_backup= n+4
else:
	n_backup= n
	

print "3.", n_backup


# 4. What is grade's letter value (eg. 90-100)
grade = raw_input("Enter a grade [0-100]: ")
grade = int(grade)

# all the cool schools grade ABCD, with no stupid + or - grades.  
# also, yayyy arrays
gradescale = ['your grade is: A','your grade is: B','your grade is: C','your grade is: D','you Failed']
your_grade = gradescale[0]

# yeah, yeah, glass houses blah.  Well, if it's going to be late, I might as well have fun with it.  The Debian of late homeworks!
spice = "if this part wasn't one of Paul's snarky add-ons, I'll look like a humorless jerk!  Also, since I'll probably have this assignment in late, kinda hipocritical"

if grade > 90:
	your_grade = gradescale[0]
	spice = "congratulations on hitting the arbitrarily defined ceiling"
elif 90 > grade > 80:
	your_grade = gradescale[1]
	spice = "congratulations on somehow being above average and mediocre simultaneously"
elif 80 > grade > 70:
	your_grade = gradescale[2]
	spice = "congratulations on being average.  This means you're a bad student and will probably lose that scholarship"
elif 70 > grade > 60:
	your_grade = gradescale[3]
	spice = "AWESOME!  If your grades are this low, you're probably on one of the sports teams we blow thousands of dollars annually on!"
else:
	your_grade = gradescale[4]
	spice = "you should probably kill yourself now.  Really, throw yourself into the gorge"

print "4.", your_grade
print spice


