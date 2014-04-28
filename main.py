import spritesheet as spritesheet
import pygame
from pygame.locals import *
 
class App:
    def __init__(self):
        self._running = True
        self._display_surf = None
        self.ss = None
        self.background = None
        self.flappy = None
        self.flappyRect = None
        self.flag=None
        self.y = 0.0
        self.g = 0.01
 
    def on_init(self):
        pygame.init()
        self._display_surf = pygame.display.set_mode((287,510), pygame.HWSURFACE)
        self._running = True
        self.ss = spritesheet.spritesheet("Flappy-Graphics.bmp")
        self.background = self.ss.image_at((0, 0, 287, 510))
        self.flappy = self.ss.image_at((230,762,33,23), colorkey=(255,255,255))
        self.flappyRect = self.flappy.get_rect()
    def on_event(self, event):
        if event.type == pygame.QUIT:
            self._running = False
        if event.type == KEYDOWN:
            if event.key == K_m:
                self.flag = 1
                
    def on_loop(self):
        if self.flag:
            self.y = -2
            self.flag = 0
        else:
            self.y = self.y + self.g
        self.flappyRect= self.flappyRect.move(0, self.y)
               
        
        
        
    def on_render(self):
        self._display_surf.blit(self.background,(0,0))
        self._display_surf.blit(self.flappy, self.flappyRect)
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
