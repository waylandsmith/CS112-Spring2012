#!/usr/bin/env python
"""
rects.py

Pygame Rectangles
=========================================================
The following section will test your knowledge of how to 
use pygame Rect, arguably pygame's best feature. Define
the following functions and test to make sure they 
work with `python run_tests.py`

Make sure to use the documentation 
http://www.pygame.org/docs/ref/rect.html


Terms:
---------------------------------------------------------
  Point:     an x,y value
               ex:  pt = 3,4

  Polygon:   a shape defined by a list of points
               ex:  poly = [ (1,2), (4,8), (0,3) ]

  Rectangle:  pygame.Rect
"""

from pygame import Rect

# 1. poly_in_rect
#      Check to see if the polygon is completely within a given 
#      rectangle.
#
#      returns:  True or False

def poly_in_rect(poly, rect):
    rTopLeft = rect.topleft
    rTopRight = rect.topright
    rBRight = rect.bottomright
    rBLeft = rect.bottomleft
    rW = rect.width
    rH = rect.height

    rTLx, rTLy = rTopLeft
    rTRx, rTRy = rTopRight
    rBRx, rBRy = rBRight
    rBLx, rBLy = rBLeft 

    polyShape = "NONE"
    if len(poly) == 3:
        polyShape = "triangle"
        pp1x, pp1y = poly[0]  # <- poly point <number> <position>, abbreviated as pp<#><letter>
        pp2x, pp2y = poly[1]
        pp3x, pp3y = poly[2]

    elif len(poly) == 4:
        polyShape = "square"
        pp1x, pp1y = poly[0]  # <- poly point <number> <position>, abbreviated as pp<#><letter>
        pp2x, pp2y = poly[1]
        pp3x, pp3y = poly[2]
        pp4x, pp4y = poly[3] 
        
    else:
        polyShape = "not a polygon"
    
    inside = True

    done = False   
    while not done:
        if polyShape.lower() in ['square']: # OTHER RECTANGLES
            if rTLx >= pp1x: # this series checks if any of the points are to the left boundary of the rectangle
                inside = False
            elif rTLx >= pp2x:
                inside = False
            elif rTLx >= pp3x:
                inside = False
            elif rTLx >= pp4x:
                inside = False
            elif rBRx <= pp1x: # this series checks if any points are right of the rectangle
                inside = False
            elif rBRx <= pp2x:
                inside = False
            elif rBRx <= pp3x:
                inside = False
            elif rBRx <= pp4x:
                inside = False
            elif rTLy >= pp1y: # this series checks if any points are to the top of the rectangle
                inside = False
            elif rTLy >= pp2y:
                inside = False
            elif rTLy >= pp3y:
                inside = False
            elif rTLy >= pp4y:
                inside = False
            elif rBLy <= pp1y: # this series checks if any points are below the rectangle.
                inside = False
            elif rBLy <= pp2y:
                inside = False
            elif rBLy <= pp3y:
                inside = False
            elif rBLy <= pp4y:
                inside = False
            else:
                inside = True
        elif polyShape.lower() in ['triangle']: # TRIANGLES
            if rTLx >= pp1x: # this series checks if any of the points are to the left boundary of the rectangle
                inside = False
            elif rTLx >= pp2x:
                inside = False
            elif rTLx >= pp3x:
                inside = False
            elif rBRx <= pp1x: # this series checks if any points are right of the rectangle
                inside = False
            elif rBRx <= pp2x:
                inside = False
            elif rBRx <= pp3x:
                inside = False
            elif rTLy >= pp1y: # this series checks if any points are to the top of the rectangle
                inside = False
            elif rTLy >= pp2y:
                inside = False
            elif rTLy >= pp3y:
                inside = False
            elif rBLy <= pp1y: # this series checks if any points are below the rectangle.
                inside = False
            elif rBLy <= pp2y:
                inside = False
            elif rBLy <= pp3y:
                inside = False
        
        done = True  

        return inside


# 2. surround_poly
#      Create a rectangle which contains the given polygon.  
#      It should return the smallest possible rectangle 
#      where poly_in_rect returns True.
#
#      returns:  pygame.Rect

# hilariously, the test program claims that rects.py is "OK" even when I had absolutely nothing in the below function.  Lulz.

def surround_poly(poly):
    "create a rectangle which surounds a polygon"
    
    xlist = []
    ylist = []
    
    done = False

    while not done:
        for point in poly[]:
            px, py = point
            xlist.append(px)
            ylist.append(py)
    

"""
    import pygame

    TLx, TLy = poly[0]
    TRx, TRy = poly[1]
    BLx, BLy = poly[2]
    BRx, BRy = poly[3]
    
    TLx = TLx * 100
    TRx = TRx * 100
    BLx = BLx * 100
    BRx = BRx * 100
    TLy = TLy * 100
    TRy = TRy * 100
    BLy = BLy * 100
    BRy = BRy * 100

    rectSize = BRx, BRy * 2
    rect = pygame.Rect((0,0), rectSize)
    return rect
