import pygame
import spritesheet

WHITE = (255,255,255)

TREE1 = [0,0,512/2, 512/2]
TREE2 = (512/2,0, 512/2, 512/2)

height = int(512 * 0.25)
width = int(512 * 0.25)

class trees(pygame.sprite.Sprite):
    
    def __init__(self):
        super().__init__()

        
        
        self.image = pygame.Surface([75,75])
        self.image.fill((255,255,255))
        self.image.set_colorkey(WHITE)

        #self.innerbounds = [self.x + 10, self.y + 10, self.x+width-10, self.y+height-10]

        #self.trees_sprites = pygame.image.load("tree.png")
        sprite_sheet = spritesheet.SpriteSheet("tree.png")
        self.image = sprite_sheet.get_image(TREE1[0], TREE1[1], TREE1[2], TREE1[3])
        self.image = pygame.transform.scale(self.image, (height, width))

        
        
        #pygame.draw.rect(self.image, (255,255,0), [0, 0, 50, 50])

        self.rect = self.image.get_rect()

        
    def get_boundaries(self):
        self.boundaries = [self.rect.x + 50, self.rect.y + 50, width - 100, height - 100]

        
    
