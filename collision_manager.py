import spritesheet as spritesheet
import pygame
from pygame.locals import *



def checkCollision(tubeUpRects, tubeDownRects, groundRect, flappyRect):
    if (flappyRect.bottom >= groundRect.top): return 1
    for rect in tubeUpRects:
        if(flappyRect.right == rect.left and flappyRect.top <= rect.bottom): return 1
        if(flappyRect.top <= rect.bottom and flappyRect.right > rect.left and flappyRect.left < rect.right): return 1
    for rect in tubeDownRects:
        if(flappyRect.right == rect.left and flappyRect.bottom >= rect.top): return 1
        if(flappyRect.bottom >= rect.top and flappyRect.right > rect.left and flappyRect.left < rect.right): return 1
    return 0
        
        
