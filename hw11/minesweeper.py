#!/usr/bin/env python

import random
import pygame
from pygame.locals import *



# SETTINGS

FPS = 30


tileSize = (60,60)
tileBorder = (61,61)

# Colors
C_BORDER = 0,0,0
C_HIDDEN = 80,80,80
C_ACTIVE = 255,255,255
C_CLEARED = 180,180,180
C_BOMB = 255,0,0

def clear_square(world,x,y):
    world[x][y]["cleared"] = True

# OBJECTS
# bounds = screen.get_rect()
# grid = [[None, None, None, 

ll = [[0,0,0,0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0,0,-,0],
      [0,0,0,0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0,0,0,0]]


"""
grid = []

y = [1,2,3,4,5,6,7,8,9,10]

row = []
col = []
for j in range(10):
    j += 1
    row.append(j)
    for i in range(10):
        i += 1
        col.append(i)


for i in range(10): # rows
    row = []
    for j in range(10): # cols
        row.append(0)
    grid.append(row)
"""
#for i in range(50):
#    x = 

"""
for i,row in enumerate(grid):
    for j, val in enumerate(row):
"""

# tile1 = pygame.Rect((0,0), tileSize)
tiles = [ (pygame.Rect((0,0), tileSize)),
          (pygame.Rect((0,0), tileSize)),
          (pygame.Rect((0,0), tileSize)),
          (pygame.Rect((0,0), tileSize)),
          (pygame.Rect((0,0), tileSize)),
          (pygame.Rect((0,0), tileSize)),
          (pygame.Rect((0,0), tileSize)),
          (pygame.Rect((0,0), tileSize)),
          (pygame.Rect((0,0), tileSize)),
          (pygame.Rect((0,0), tileSize)),
          (pygame.Rect((0,0), tileSize)),
          (pygame.Rect((0,0), tileSize)),
         ]




# FUNCTIONS
def build_floor(width,height,num_bombs):
    "the TAs put this on the board"
    # create grid
    level = []
    for y in range(height):
        row = []
        for x in range(width):
            row.append(0)
        level.append(row)
        
        # place bombs
        bombs = 0
        while bombs < num_bombs:
            x = random.randrange(width)
            y = random.randrange(height)
            if not level[y][x]:
                level[y][x] = -1
                bombs += 1

        # calculate number of bombs touching

        return level

# Initialize
pygame.init()
wmCap = pygame.display.set_caption(title)
screen = pygame.display.set_mode(screenSize)





# GAME LOOP

done = False
while not done:
    for event in pygame.event.get():
        if event.type == QUIT:
            done = True
        elif event.type == KEYDOWN and event.key == K_ESCAPE:
            done = True

    # Draw

    screen.fill(backGround)
    for 



    pygame.display.flip()


print "Pygame:  now with window titles.  Get yours today!"



# Multi-dimensional lists
# you put a list inside a list
# for loops inside for loops
