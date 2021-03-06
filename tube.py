import spritesheet as spritesheet
import random as random
from collections import deque
import pygame
from pygame.locals import *

class tube():

    def __init__(self, flappyss):
        self.upRects = deque()
        self.downRects = deque()
        yUP = 0
        yDown = 0
        self.tubeDownSprite = flappyss.image_at((168, 646, 52, 320), colorkey = (255, 255, 255))
        self.tubeUpSprite = flappyss.image_at((112, 646, 52, 320), colorkey = (255, 255, 255))
        for i in range (0, 4):
            yDown = random.randint(150, 440)
            yUp = yDown - 450
            self.upRects.append(self.tubeUpSprite.get_rect())
            self.downRects.append(self.tubeDownSprite.get_rect())
            if i == 0:
                self.upRects[i].move_ip(330, yUp)
                self.downRects[i].move_ip(330, yDown)
            else:
                self.upRects[i].move_ip(self.upRects[i-1].right + 100, yUp)
                self.downRects[i].move_ip(self.upRects[i-1].right + 100, yDown)
                
    def restart(self):
        for i in range (0, 4):
            yDown = random.randint(150, 440)
            yUp = yDown - 450
            self.upRects[i] = self.tubeUpSprite.get_rect()
            self.downRects[i]= self.tubeDownSprite.get_rect()
            if i == 0:
                self.upRects[i].move_ip(330, yUp)
                self.downRects[i].move_ip(330, yDown)
            else:
                self.upRects[i].move_ip(self.upRects[i-1].right + 100, yUp)
                self.downRects[i].move_ip(self.upRects[i-1].right + 100, yDown)
        
                
    def normalMovement(self):
        if(self.upRects[0].right <= 0):
            yDown = random.randint(150, 440)
            yUp = yDown - 450
            self.upRects.rotate(-1)
            self.downRects.rotate(-1)
            self.upRects[3] = self.tubeUpSprite.get_rect()
            self.upRects[3].move_ip(self.upRects[2].right + 100, yUp)
            self.downRects[3] = self.tubeDownSprite.get_rect()
            self.downRects[3].move_ip(self.upRects[2].right + 100, yDown)
            
        for i in range (0, 4):
            self.upRects[i] = self.upRects[i].move(-1, 0)
            self.downRects[i] = self.downRects[i].move(-1, 0)
        

                    
           

            
        
        
    
            
        
