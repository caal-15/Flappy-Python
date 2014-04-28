import spritesheet as spritesheet
import pygame
from pygame.locals import *
 
class flappy():
    def __init__(self, flappyss):
        self.x = 287/2
        self.y = 0
        self.g = 1
        self.flappyRect = None
        self.flappySprite = flappyss.image_at((230,762,33,23), colorkey=(255,255,255))
        self.flappyRect = self.flappySprite.get_rect()
        
