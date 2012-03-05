#!/usr/bin/env python
"""
tron.py

The simple game of tron with two players.  Press the space bar to start the game.  Player 1 (red) is controlled with WSAD and player 2 (blue) is controlled with the arrow keys.  Once the game is over, press space to reset and then again to restart.  Escape quits the program.
"""

import pygame
from pygame.locals import *

class

#def kill():


pygame.init()
screen = pygame.display.set_mode()
bounds = screen.get_rect()
clock = pygame.time.Clock()
done = False

while not done:

    pygame.display.flip()
