import pygame
import math
import random

WHITE = (255,255,255)

width = 75
height = 81
speed = 0

class zombie(pygame.sprite.Sprite):
    
    def __init__(self):
        super().__init__()

        self.image = pygame.Surface([75,81])
        self.image.fill((255,255,255))
        self.image.set_colorkey(WHITE)
        
        #pygame.draw.rect(self.image, (255,255,0), [0, 0, 50, 50])
        self.image = pygame.image.load("zombie sprite.gif").convert_alpha()
        self.original_image = self.image

        self.speed = random.uniform(0,1)

        self.rect = self.image.get_rect()        
    

    def face_player(self, player):
        self.image = self.original_image
        self.rect = self.image.get_rect(center=self.rect.center)
        
        zombie_centre = self.rect.center
        player_centre = player.rect.center

        angle = math.degrees(math.atan2(zombie_centre[0]-player_centre[0], zombie_centre[1]-player_centre[1]))+90
        angle = angle+random.randint(-10,10)
        self.image = pygame.transform.rotate(self.image, angle)
        self.rect = self.image.get_rect(center=self.rect.center)

    def move_to_player(self, player):
        zombie_centre = self.rect.center
        player_centre = player.rect.center

        if zombie_centre != player_centre:
        
            dx, dy = (player_centre[0] - zombie_centre[0], player_centre[1] - zombie_centre[1])

            stepx, stepy = ((dx/60)*self.speed, (dy/60)*self.speed)
            if stepx > 0:
                stepx += 1
            else:
                stepx -= 1
            if stepy > 0:
                stepy += 1
            else:
                stepy -= 1
            
            stepx = int(stepx)
            stepy = int(stepy)

            self.rect.centerx = self.rect.centerx + stepx
            self.rect.centery = self.rect.centery + stepy

        
        
