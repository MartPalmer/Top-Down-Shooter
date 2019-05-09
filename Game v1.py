import pygame
import player
import trees
import random
import zombie

pygame.init()

#set up variables
size = (800,600)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Zombie Shooter")

BLACK = (0,0,0)
WHITE = (255,255,255)
GREEN = (0,255,0)
RED = (255,0,0)
BLUE = (0,0,255)

#set up functions

all_sprites_list = pygame.sprite.Group()

screen.fill(WHITE)
p = player.player()
p.rect.x = 100
p.rect.y = 100
all_sprites_list.add(p)

bg = pygame.image.load("bg1.png")

z = []
for i in range(0,10):
    z.append(zombie.zombie())
    randx = 0
    randy = 0
    
    while randx < 150 and randy < 150:
        randx = random.randint(0,800)
        randy = random.randint(0,600)

    z[i].rect.x = randx
    z[i].rect.y = randy
    all_sprites_list.add(z[i])

t = []
for i in range(0,25):
    t.append(trees.trees())
    randx = 0
    randy = 0

    while randx < 150 and randy < 150:
        randx = random.randint(0,800)
        randy = random.randint(0,600)
        
    t[i].rect.x = randx
    t[i].rect.y = randy
    all_sprites_list.add(t[i])



carryOn = True
clock = pygame.time.Clock()
seconds = 0
player_speed = 3

# Check for events
while carryOn:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            carryOn = False

    #if included in the for loop it won't keep repeating the movement and just move once
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_a:
            if p.sprites_touching(t):
                p.moveLeft(player_speed)
            else:
                p.moveRight(player_speed*2)
        elif event.key == pygame.K_s:
            if p.sprites_touching(t):
                p.moveDown(player_speed)
            else:
                p.moveUp(player_speed*2)
        elif event.key == pygame.K_d:
            if p.sprites_touching(t):
                p.moveRight(player_speed)
            else:
                p.moveLeft(player_speed*2)                
        elif event.key == pygame.K_w:
            if p.sprites_touching(t):
                p.moveUp(player_speed)
            else:
                p.moveDown(player_speed*2)      
        

    #Game logic goes here
    for i in range(0,len(z)): 
        z[i].face_player(p)
        z[i].move_to_player(p)
        
    all_sprites_list.update()

    #Drawing goes here

    #tile the background to fill the screen
    for i in range(0,3):
        for j in range (0, 4):
            screen.blit(bg, (j*245,i*226))
            #245 and 226 are the height and width of the image
    
    all_sprites_list.draw(screen)
    #pygame.draw.rect(screen, RED, p.rect)
    #pygame.draw.rect(screen, GREEN, z.rect)

    #update the screen with what it drawn
    pygame.display.flip()

    #set fps, wait untill next frame
    seconds += 1
    clock.tick(60)

print("Quiting")
pygame.quit()


            

