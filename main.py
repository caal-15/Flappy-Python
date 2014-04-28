import spritesheet as spritesheet
import flappy as flappy
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
        self.clock = pygame.time.Clock()
 
    def on_init(self):
        pygame.init()
        self._display_surf = pygame.display.set_mode((287,510), pygame.HWSURFACE)
        self._running = True
        self.ss = spritesheet.spritesheet("Flappy-Graphics.bmp")
        self.background = self.ss.image_at((0, 0, 287, 510))
        self.flappy = flappy.flappy(self.ss)
                

    def on_event(self, event):
        if event.type == pygame.QUIT:
            self._running = False
        if event.type == KEYDOWN:
            if event.key == K_m:
                self.flag = 1
                
    def on_loop(self):
        self.clock.tick(60)
        if self.flag:
            self.flappy.y = -12
            self.flag = 0
        else:
            self.flappy.y = self.flappy.y + self.flappy.g
        self.flappy.flappyRect= self.flappy.flappyRect.move(0, self.flappy.y)

        
    def on_render(self):
        self._display_surf.blit(self.background,(0,0))
        self._display_surf.blit(self.flappy.flappySprite, (self.flappy.x, self.flappy.flappyRect.top))
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
