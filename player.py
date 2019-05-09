import pygame

WHITE = (255,255,255)

width = 50
height = 50

class player(pygame.sprite.Sprite):
    
    def __init__(self):
        super().__init__()

        self.image = pygame.Surface([50,50])
        self.image.fill((255,255,255))
        self.image.set_colorkey(WHITE)

        self.character_up = pygame.image.load("c1_up1.png").convert_alpha()
        self.character_down = pygame.image.load("c1_down1.png").convert_alpha()
        self.character_left = pygame.image.load("c1_left1.png").convert_alpha()
        self.character_right = pygame.image.load("c1_right1.png").convert_alpha()
        
        #pygame.draw.rect(self.image, (255,255,0), [0, 0, 50, 50])
        self.image = self.character_up
        

        self.rect = self.image.get_rect()

        

    def moveRight(self, pixels):
        self.image = self.character_right
        self.rect.centerx += pixels
        

    def moveLeft(self, pixels):
        self.image = self.character_left
        self.rect.centerx -= pixels

    def moveUp(self, pixels):
        self.image = self.character_up
        self.rect.centery -= pixels
        


    def moveDown(self, pixels):
        self.image = self.character_down
        self.rect.centery += pixels
        

    def sprites_touching(self, obstacles):
        counter = 0
        for each_obstacle in obstacles:
            each_obstacle.get_boundaries()
            if (self.rect.x < (each_obstacle.boundaries[0] + each_obstacle.boundaries[2])) and ((self.rect.x + width) > each_obstacle.boundaries[0]) and (self.rect.y < (each_obstacle.boundaries[1] + each_obstacle.boundaries[3])) and ((self.rect.y + height) > (each_obstacle.boundaries[1])):
                counter += 1

        if counter > 0:
            return False
        else:        
            return True

    
    
