import pygame
import sys
pygame.init
 
class spritesheet(object):
    def __init__(self, filename):
        try:
            self.sheet = pygame.image.load(filename).convert()
        except pygame.error, message:
            print 'Unable to load spritesheet image:', filename
            raise SystemExit, message
    # Load a specific image from a specific rectangle
    def image_at(self, rectangle, colorkey = None):
        "Loads image from x,y,x+offset,y+offset"
        rect = pygame.Rect(rectangle)
        image = pygame.Surface(rect.size).convert()
        image.blit(self.sheet, (0, 0), rect)
        if colorkey is not None:
            if colorkey is -1:
                colorkey = image.get_at((0,0))
            image.set_colorkey(colorkey, pygame.RLEACCEL)
        return image
    # Load a whole bunch of images and return them as a list
    def images_at(self, rects, colorkey = None):
        "Loads multiple images, supply a list of coordinates" 
        return [self.image_at(rect, colorkey) for rect in rects]
    # Load a whole strip of images
    def load_strip(self, rect, image_count, colorkey = None):
        "Loads a strip of images and returns them as a list"
        tups = [(rect[0]+rect[2]*x, rect[1], rect[2], rect[3])
                for x in range(image_count)]
        return self.images_at(tups, colorkey)
size = width, height = 1000, 700
screen= pygame.display.set_mode(size)
x = 3
y = 3
ymov = 0
g = 0.2  
counter = 0       
ss = spritesheet('Flappy-Graphics.bmp')

image = ss.image_at((0,0, 287, 510))
image2 = ss.image_at((230, 762, 33, 23), colorkey=(255, 255, 255))
rect = image2.get_rect()
while 1:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT: 
            sys.exit()
    if rect.bottom == 510:
        y=0.8*y
        x=0.6*x
    if (g<0 and (y<=0 or rect.top < 0)) or (g>0 and rect.bottom < 510):
        g=0.2
        y=y+g
        ymov=y
        
    else:
        g=-0.2
        y=y+g
        ymov=-y
    if(rect.left<0 or rect.right>287):
        x=-x
    
    if 510 - rect.bottom <= 0.5:
        counter=counter+1
    else:
        counter=0
    if counter > 16:
        x=0
    
    rect=rect.move(x,ymov)
    screen.blit(image, (0, 0))
    screen.blit(image2, rect)
    pygame.display.flip()

        
        
