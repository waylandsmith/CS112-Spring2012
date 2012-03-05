#!/usr/bin/env python

from random import randrange
import random
import pygame
from pygame.locals import *
import os

## Settings

FPS = 30

title = "Serpent Sweeper"
screenSize = 600,600
red = 255,0,0
green = 0,255,0
blue = 0,0,255
black = 0,0,0
backGround = 0,200,100



# Colors
C_BORDER = 0,0,0
C_HIDDEN = 80,30,90
C_ACTIVE = 255,0,255
C_CLEARED = 180,180,180
C_BOMB = 255,0,0

def clear_square(world,x,y):
    world[x][y]["cleared"] = True


## Game
def game(tile, width, height, num_bombs):
    # init
    wmCap = pygame.display.set_caption(title)
    screen = pygame.display.set_mode((width*tile, height*tile))
    # store all the game data
    world = []
    for x in range(width):
        row = []
        for y in range(height):
            cell = {}
            cell["exploded"] = False
            cell["bomb"] = False
            cell["rect"] = pygame.Rect(x*tile, y*tile, tile, tile)
            cell["cleared"] = False
            row.append(cell)
        world.append(row)



    # place bombs
    c = 0
    while c < num_bombs:
        x = randrange(width)
        y = randrange(height)
        if not world[x][y]["bomb"]:
            world[x][y]["bomb"] = True
            c += 1
    
    # win condition
    winCount = (height * width) - num_bombs
    if winCount == 0:
        print "you win!"


    ## flags
    lmb_clicked = False
    action_clear_square = False

    # loop
    clock = pygame.time.Clock()
    done = False
    while not done:
        # input
        for event in pygame.event.get():
            if event.type == QUIT:
                done = True
            elif event.type == KEYDOWN and event.key == K_ESCAPE:
                done = True

            # mouse
            elif event.type == MOUSEBUTTONDOWN and event.button == 1:
                lmb_clicked = True
            elif event.type == MOUSEBUTTONUP and event.button == 1:
                lmb_clicked = False
                action_clear_square = True




               # for world[x][y]["bomb"] in ():
        # update
        if action_clear_square:
            x,y = pygame.mouse.get_pos()
            x /= tile
            y /= tile
            clear_square(world, x, y)
            action_clear_square = False

### DOESN'T WORK YET           
            # finds the number of bombs adjacent
 #           for x in range(width):
 #               for y in range(height):
 #                   finished = False
 #                   if world[x][y]["cleared"] == True:
 #                       while not finished:
 #                           numAdj = 0

#                            if world[x][y-1]["bomb"] == True:
#                                numAdj += 1
#                            if world[x][y+1]["bomb"] == True:
#                                numAdj += 1
#                            if world[x+1][y]["bomb"] == True:
#                                numAdj += 1
#                            if world[x+1][y+1]["bomb"] == True:
#                                numAdj += 1
#                            if world[x+1][y-1]["bomb"] == True:
#                                numAdj += 1
#                            if world[x-1][y]["bomb"] == True:
#                                numAdj += 1
#                            if world[x-1][y-1]["bomb"] == True:
#                                numAdj += 1
#                            if world[x-1][y+1]["bomb"] == True:
#                                numAdj += 1

#                            print numAdj
#                            finished = True
        
            if world[x][y]["bomb"]:
                world[x][y]["exploded"] = True
                print x,y
                for x in range(width):
                    for y in range(height):
                        world[x][y]["cleared"] = True
                print "you lose!"

            for world[x][y]["cleared"] in range(width):
                for world[x][y]["cleared"] in range(height):
                    winCount -=  1

        # display
        screen.fill(C_BORDER)

        # draw each cell
        for x in range(width):
            for y in range(height):
                # get rect for cell
                rect = world[x][y]["rect"]

                # color for cell
                if world[x][y]["cleared"]:
                    bg_color = C_CLEARED

                elif lmb_clicked and rect.collidepoint(pygame.mouse.get_pos()):
                    bg_color = C_ACTIVE
                else:
                    bg_color = C_HIDDEN

                # draw background
                screen.fill(bg_color, rect.inflate(-2, -2))


                # draw cleared graphics
                if world[x][y]["cleared"]:
                    if world[x][y]["bomb"]:
                        pygame.draw.ellipse(screen, C_BOMB, rect.inflate(-tile/2, -tile/2))  
                        
                if world[x][y]["exploded"]:
                    bg_color = red
                       # for Xx in range(width):
                       #     for Xy in range(height):
                       #         pygame.draw.rect(screen, red, rect.inflate(tile, tile))


        # refresh
        pygame.display.flip()
        clock.tick(FPS)



# Application
def main():
    pygame.init()
    game(50, 10, 10, 10)


main()
print "Pygame:  now with window titles!  Get yours today"


"""
        finished = False
        for k in world[x][y]["cleared"]:
            for l in world[x][y]["cleared"]:
                while not finished:
                    numAdj = 0
                    if world[x][y-1]["bomb"] == True:
                        numAdj += 1
                    if world[x][y+1]["bomb"] == True:
                        numAdj += 1
                    if world[x+1][y]["bomb"] == True:
                        numAdj += 1
                    if world[x+1][y+1]["bomb"] == True:
                        numAdj += 1
                    if world[x+1][y-1]["bomb"] == True:
                        numAdj += 1
                    if world[x-1][y]["bomb"] == True:
                        numAdj += 1
                    if world[x-1][y-1]["bomb"] == True:
                        numAdj += 1
                    if world[x-1][y+1]["bomb"] == True:
                        numAdj += 1

                    print numAdj
                    finished = True        
"""











