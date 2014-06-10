import spritesheet as spritesheet
import flappy as flappy
import tube as tube
import ground as ground
import pygame
from pygame.locals import *

class App:
    def __init__(self):
        self._running = True
        self._display_surf = None
        self.ss = None
        self.background = None
        self.flag=None
        self.flappy = None
        self.tube = None
        self.ground = None
        self.clock = pygame.time.Clock()
        self.numbers = None
        self.numberRect = None 
        self.score = None
        self.menu = None
        self.title = None
        
 
    def on_init(self):
        pygame.init()
        self._display_surf = pygame.display.set_mode((287,510), pygame.HWSURFACE)
        pygame.display.set_caption("Annoying Bird 0.5")
        self._running = True
        self.ss = spritesheet.spritesheet("Flappy-Graphics.bmp")
        self.numbers = self.ss.images_at([(276,647,11,13), (276,665,11,13), (276,699,11,13), (276,717,11,13), (276,751,11,13), (276,769,11,13), (276,803,11,13), (276,821,11,13), (276,855,11,13), (276,873,11,13)], colorkey =(255,255,255))
        self.background = self.ss.image_at((0, 0, 287, 510))
        self.score = 0
        self.numberRect = self.numbers[0].get_rect().move(125, 30)
        self.flappy = flappy.flappy(self.ss)
        self.tube = tube.tube(self.ss)
        self.ground = ground.ground(self.ss)
        self.menu = True
        self.title = pygame.image.load("Menu.bmp")
        pygame.mixer.init()
        pygame.mixer.music.load("TOP.ogg") 
        pygame.mixer.music.set_volume(1.0)
        
 
    def scoreUpdate(self):
        for rect in self.tube.upRects:
            if(rect.right == self.flappy.flappyRect.left): self.score= self.score + 1 
           
    def checkCollision(self):
        if (self.flappy.flappyRect.bottom >= self.ground.groundRects[0].top): return 1
        for rect in self.tube.upRects:
            if(self.flappy.flappyRect.right == rect.left and self.flappy.flappyRect.top <= rect.bottom): return 1
            if(self.flappy.flappyRect.top <= rect.bottom and self.flappy.flappyRect.right > rect.left and self.flappy.flappyRect.left < rect.right): return 1
        for rect in self.tube.downRects:
            if(self.flappy.flappyRect.right == rect.left and self.flappy.flappyRect.bottom >= rect.top): return 1
            if(self.flappy.flappyRect.bottom >= rect.top and self.flappy.flappyRect.right > rect.left and self.flappy.flappyRect.left < rect.right): return 1
        return 0   
    
    def on_event(self, event):
        if event.type == pygame.QUIT:
            self._running = False
        if event.type == KEYDOWN:
            if event.key == K_SPACE:
                self.flag = 1
                if self.menu == True:
                    self.menu = False
                    self.restart()
                    pygame.mixer.music.play(1, 1.5)
            elif event.key == K_s and self.menu == True:
                pygame.mixer.music.stop()
                pygame.mixer.music.play(1, 1.5)
    
    def restart(self):
        self.tube.restart()
        self.flappy.restart()
        pygame.mixer.music.stop()
        self.score = 0
                
    def on_loop(self):
        self.clock.tick(60)
        if self.menu == False:
            if (self.checkCollision()): 
                self.restart()
                self.menu = True
            self.scoreUpdate()    
            self.flappy.normalMovement(self.flag)
            self.ground.normalMovement()
            self.tube.normalMovement()
            if self.flag: self.flag = 0
        
        if self.menu == True:
            pass

        
    def on_render(self):
        if self.menu == False:
            self._display_surf.blit(self.background,(0,0))
            self._display_surf.blit(self.flappy.actualSprite, self.flappy.flappyRect)
            for i in range (0,4):
                self._display_surf.blit(self.tube.tubeUpSprite, self.tube.upRects[i])
                self._display_surf.blit(self.tube.tubeDownSprite, self.tube.downRects[i])
            self._display_surf.blit(self.ground.groundSprite, self.ground.groundRects[0])
            self._display_surf.blit(self.ground.groundSprite, self.ground.groundRects[1])
            self._display_surf.blit(self.numbers[self.score/10], self.numberRect)
            self._display_surf.blit(self.numbers[self.score % 10], (self.numberRect.right + 5, self.numberRect.top))
        if self.menu == True:
            self._display_surf.blit(self.background,(0,0))
            self._display_surf.blit(self.title,(0,0))

        pygame.display.flip()
    
    def on_cleanup(self):
        pygame.quit()
 
    def on_execute(self):
        if self.on_init() == False:
            self._running = False
 
        while( self._running ):
            for event in pygame.event.get():
                self.on_event(event)
            self.on_loop()
            self.on_render()
        self.on_cleanup()
 
if __name__ == "__main__" :
    theApp = App()
    theApp.on_execute()
