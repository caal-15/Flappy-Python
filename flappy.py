import spritesheet as spritesheet
import pygame
from pygame.locals import *
 
class flappy():
    def __init__(self, flappyss):
        self.x = 266/2
        self.y = 0
        self.g = 1
        self.flappyRect = None
        self.flappySprites = flappyss.images_at([(230,762,33,23), (230, 814, 33, 23), (230, 866, 33, 23)], colorkey =(255,255,255))
        self.actualSprite = self.flappySprites[0]
        self.flappyRect = self.flappySprites[0].get_rect().move(self.x, 0)
        self.counter = 0
        
        
    def normalMovement(self, flag):
        if self.counter > 2: self.counter = 0
        self.actualSprite = self.flappySprites[self.counter]
        self.counter = self.counter + 1
        if flag:
            self.y = -12
            
        else:
            self.y = self.y + self.g
        self.flappyRect= self.flappyRect.move(0, self.y)
        if self.flappyRect.bottom >= 511 : 
            self.flappyRect= self.flappyRect.move(0, -250)
            self.y = 0
        
