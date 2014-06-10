import spritesheet as spritesheet
import pygame
from pygame.locals import *
 
class flappy():
    def __init__(self, flappyss):
        self.x = 266/2
        self.y = 0
        self.g = 1
        self.angle = -45;
        self.flappySprites = flappyss.images_at([(230,762,33,23), (230, 814, 33, 23), (230, 866, 33, 23)], colorkey =(255,255,255))
        self.rotationSprite = self.flappySprites[0] #surface temporal para rotar a flappy
        self.actualSprite = self.rotationSprite #surface con flappy rotado
        self.flappyRect = self.flappySprites[0].get_rect().move(self.x, 0)
        self.counter = 0
        self.fskpr = 0 #se saltara frames para hacer mas lenta la animacion
        
        
    def normalMovement(self, flag):
        if self.counter > 2: self.counter = 0
        self.rotationSprite = self.flappySprites[self.counter]
        self.angle = -3*self.y
        self.actualSprite = pygame.transform.rotate(self.rotationSprite, self.angle)
        
        if not(self.fskpr < 2):
            self.counter = self.counter + 1
            self.fskpr = 0
        self.fskpr +=1

        if flag:
            self.y = -11
            
        else:
            self.y = self.y + self.g
        self.flappyRect= self.flappyRect.move(0, self.y)
        
        
    def restart(self):
        self.flappyRect = self.flappySprites[0].get_rect().move(self.x, 200)    
        
        
    
        
