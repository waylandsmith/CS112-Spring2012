#!/usr/bin/env python

import math
from random import randrange

import pygame
from pygame import Rect, Surface
from pygame.locals import *
from pygame.sprite import Sprite, Group

from app import Application
from graphics import draw_tie, draw_ywing
from ships import Ship, ShipSpawner
from utils import *


## SHIP GROUP

class ShipGroup(Group):
    def __init__(self, count):
        Group.__init__(self)
    self.count = count
    
    def add(self, *sprites):
        for sprite in sprites:
            if len(self) < self.count:
                Group.add(self, sprite)

class Game(Application):
    title = "Spaceships"
    screen_size = 800, 600

    def __init__(self):
        Application.__init__(self)
        
        self.bounds = self.screen.get_rect()
        self.ships = Group()
        
        self.spawners = [ ShipSpawner(2000, self.ships, self.bounds) ]
        
    def update(self):
        dt = self.clock.get_time()
        
        self.ships.update(dt)
        
        for spawner in self.spawners:
            spawner.update(dt)
            
    def draw(self, screen):
        screen.fill((0,0,0))
        self.ships.draw(screen)

if __name__ == "__main__":
    Game().run()
    print "ByeBye"
    

class TieFighter(Ship):
    width = 40
    height = 40
    
    def draw_image(self):
        draw_tie(self.image, self.color)
        
class TieSpawner(ShipSpawner):
    ship_type = TieFighter
    
    def rand_vel(self):
        vx = randint_neg(100, 250)
        vy = randint_neg(100, 250)
        return vx, vy

        
    def rand_color(self):
        r = randrange(128,256)
        return r,0,0
        
        
