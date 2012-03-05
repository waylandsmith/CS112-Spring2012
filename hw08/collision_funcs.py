#!/usr/bin/python env

# Calculate if a point is within a box
#    check if a point is inside a given box.  
#
#    Parameters:
#       pt: list of 2 numbers (x,y)
#       box: list of 4 numbers (x,y,w,h).  x,y is the top left point.  w,h is the width and height

def point_in_box(pt, box):
    xpt,ypt = pt
    xb,yb,w,h = box
    inside = False
    if (xpt < xb + w) and (xpt >= xb) and (ypt < yb + h) and (ypt >= h):
        inside = True
    return inside

# the below didn't work.....not really sure why.  
"""
    inside = False
    done = False
    inside = False
    while not done:
        if xb >= xpt:
            inside = False
        elif yb <= ypt:
            inside = False
        elif (xb + w) <= xpt:
            inside = False
        elif (yb + h) <= ypt:
            inside = False
        else:
            inside = True
        done = True    

"""

