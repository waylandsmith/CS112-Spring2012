#!/usr/bin/env python

# Create a greeter
#    create a greeter that says hello to someone in all lower case.  Use print statements
#
#  ex:
#   >>> greeter("paul")
#   hello, paul
#   >>> greeter(3)
#   hello, 3
#   >>> greeter("WORLD")
#   hello, world

# def greeter(name):
def greeter(name):
    name = str(name)
    name = name.lower()
    print "hello,",name

# Draw a box
#    given a width and a height, draw a box in the terminal.  Use print statements
#
#  ex:
#    >>> box("apples", -3)
#    Error: Invalid Dimensions
#    >>> box(1,1)
#    +
#    >>> box(4,2)
#    +--+
#    +--+
#    >>> box(3,3)
#    +-+
#    | |
#    +-+


def box(w,h):
    # having me "figure out" that the desired end behavior is something else should I have the temerity to format my output differently is not a good use of time
    # It'd be different if you explicity stated the rules, instead of providing examples, which are instances of acceptable behavior, not cut-and-dried.
    # punishing creativity makes me a mad Matt.
#    if type(w) != int


    if w <= 0 or h <= 0:
        print "Error: Invalid Dimensions"
        return
    elif w == 1:
        ceiling = "+"
    edgy=
    corners = 
    while w > 0:
        outBox += "+"

    print outBox
#    while w 


# ADVANCED
# Draw a Festive Tree
#    draw a festive tree based on the specifications.  You will need to discover the arguments 
#    and behavior by running the unittests to see where it fails.  Return a string, do not print.
#
#  ex:
#    >>> print tree()
#        *
#        ^
#       ^-^
#      ^-^-^
#     ^-^-^-^
#    ^-^-^-^-^
#       | |
#       | |

# def tree()

