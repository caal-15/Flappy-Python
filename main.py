import spritesheet as spritesheet
import flappy as flappy
import tube as tube
import collision_manager as collision
import ground as ground
import collision_manager as collision
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
 
    def on_init(self):
        pygame.init()
        self._display_surf = pygame.display.set_mode((287,510), pygame.HWSURFACE)
        self._running = True
        self.ss = spritesheet.spritesheet("Flappy-Graphics.bmp")
        self.background = self.ss.image_at((0, 0, 287, 510))
        self.flappy = flappy.flappy(self.ss)
        self.tube = tube.tube(self.ss)
        self.ground = ground.ground(self.ss)      

    def on_event(self, event):
        if event.type == pygame.QUIT:
            self._running = False
        if event.type == KEYDOWN:
            if event.key == K_m:
                self.flag = 1
    
    def restart(self):
        self.tube.restart()
        self.flappy.restart()
                
    def on_loop(self):
        self.clock.tick(60)
        if (collision.checkCollision(self.tube.upRects, self.tube.downRects, self.ground.groundRects[0], self.flappy.flappyRect)): self.restart()
        self.flappy.normalMovement(self.flag)
        self.ground.normalMovement()
        self.tube.normalMovement()
        if self.flag: self.flag = 0

        
    def on_render(self):
        self._display_surf.blit(self.background,(0,0))
        self._display_surf.blit(self.flappy.actualSprite, self.flappy.flappyRect)
        for i in range (0,4):
            self._display_surf.blit(self.tube.tubeUpSprite, self.tube.upRects[i])
            self._display_surf.blit(self.tube.tubeDownSprite, self.tube.downRects[i])
        self._display_surf.blit(self.ground.groundSprite, self.ground.groundRects[0])
        self._display_surf.blit(self.ground.groundSprite, self.ground.groundRects[1])
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
