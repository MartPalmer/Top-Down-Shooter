import pygame
import random

pygame.init()

#set up variables
size = (800,600)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Tiles Example")

BLACK = (0,0,0)
WHITE = (255,255,255)
GREEN = (0,255,0)
RED = (255,0,0)
BLUE = (0,0,255)

class tile(pygame.sprite.Sprite):

    possible_x = [150, 250, 350, 450]
    x = 0
    y = 0
    width = 100
    height = 30
    speed = 3
    
    def __init__(self):
        super().__init__()
        self.x = random.choice(self.possible_x)
        self.y = 100

        self.image = pygame.Surface([self.width,self.height])
        if self.x == 150:
            self.image.fill(BLUE)
        else:
            self.image.fill(RED)
            
        #self.image.set_colorkey(WHITE) #Sets a transparent colour
        
        pygame.draw.rect(self.image, RED, [self.x, self.y, self.width, self.height])

        self.rect = self.image.get_rect()

    def update_y(self):
        self.rect.y += self.speed

    def check_off_screen(self):
        if self.rect.y >= 500:
            return True
        else:
            return False



#set up functions

all_sprites_list = pygame.sprite.Group()

screen.fill(WHITE)

t = []
t.append(tile())
t[0].rect.x = t[0].x
t[0].rect.y = t[0].y
all_sprites_list.add(t[0])


carryOn = True
clock = pygame.time.Clock()
seconds = 0
player_speed = 3
counter = 0
tiles_counter = 1

# Check for events
while carryOn:
    #Game control algorithm
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            carryOn = False        
        

    #Game logic goes here
    
    for loop_counter in range(0, len(t)):
        t[loop_counter].update_y()

    if t[0].check_off_screen():
        all_sprites_list.remove(t[0])

        if tiles_counter > 1:
            t.remove(t[0])
            tiles_counter -= 1

    if counter == 10:
        tiles_counter = tiles_counter + 1
        t.append(tile())
        t[tiles_counter-1].rect.x = t[tiles_counter-1].x
        t[tiles_counter-1].rect.y = t[tiles_counter-1].y
        all_sprites_list.add(t[tiles_counter-1])
        counter = 0

    
        
    #all_sprites_list.update() #Maybe don't need this

    #Drawing goes here
    screen.fill(WHITE)
    all_sprites_list.draw(screen)
    


    #update the screen with what it drawn
    pygame.display.flip()

    print(tiles_counter)
    counter += 1

    #set fps, wait untill next frame
    clock.tick(30)

print("Quiting")
pygame.quit()


            

