import pygame
import math

pygame.init()

BLACK = (0,0,0)
WHITE = (255,255,255)
GREEN = (0,255,0)
RED = (255,0,0)
BLUE = (0,0,255)

class arrow(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface([255,201])
        self.image.fill((255,255,255))
        self.image.set_colorkey(WHITE)
        
        #pygame.draw.rect(self.image, (255,255,0), [0, 0, 50, 50])
        self.image = pygame.image.load("arrow.png").convert_alpha()
        self.original_image = self.image

        self.rect = self.image.get_rect()

    def face_mouse(self):
        mouse_pos = pygame.mouse.get_pos()
        self.image = self.original_image
        self.rect = self.image.get_rect(center=self.rect.center)
        arrow_pos = self.rect.center

        angle = math.degrees(math.atan2(arrow_pos[0]-mouse_pos[0], arrow_pos[1]-mouse_pos[1]))+90

        self.image = pygame.transform.rotate(self.image, angle)
        self.rect = self.image.get_rect(center=self.rect.center)
        print(self.rect.center)

    def move_arrow(self):
        mouse_pos = pygame.mouse.get_pos()
        arrow_pos = self.rect.center
        
        dx, dy = (mouse_pos[0] - arrow_pos[0], mouse_pos[1] - arrow_pos[1])
        stepx, stepy = (dx/60, dy/60)

        self.rect.centerx = self.rect.centerx + stepx
        self.rect.centery = self.rect.centery + stepy
        



#main


size = (800,600)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Zombie Shooter")
screen.fill(WHITE)

all_sprites_list = pygame.sprite.Group()

a = arrow()
a.rect.x = 500
a.rect.y = 400
all_sprites_list.add(a)
        
carryOn = True
clock = pygame.time.Clock()

# Check for events
while carryOn:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            carryOn = False

#Game logic goes here
    a.face_mouse()
    a.move_arrow()
    all_sprites_list.update()

    #Drawing goes here
    screen.fill(WHITE)
    
    all_sprites_list.draw(screen)

    #update the screen with what it drawn
    pygame.display.flip()

    #set fps, wait untill next frame
    clock.tick(60)

print("Quiting")
pygame.quit()
    
