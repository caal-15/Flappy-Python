import spritesheet as spritesheet
import random as random
import pygame
from pygame.locals import *

class ground():

    def __init__(self, flappyss):
        self.groundSprite = flappyss.image_at((585, 0, 335, 113), colorkey = (255, 255, 255))
        self.y = 450
        self.groundRects = [self.groundSprite.get_rect().move(0, 450), self.groundSprite.get_rect().move(334, 450)]
        
    def normalMovement(self):
        if(self.groundRects[1].left == 0):
            self.groundRects[0] = self.groundRects[1]
            self.groundRects[1] = self.groundRects[0].move(334, 0)
        self.groundRects[0] = self.groundRects[0].move(-1, 0)
        self.groundRects[1] = self.groundRects[1].move(-1, 0)
