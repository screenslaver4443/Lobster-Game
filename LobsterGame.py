# Miss Hocking
# Lobster Game
# Including images and collisions between characters
# 20/08/2020

import pygame
import random
pygame.init()

class lobster():
    """ This is the main character of the game """
    def __init__(self):
        self.x = 100
        self.y = 100
        self.speedX = 0 
        self.speedY = 0
        self.size = 80
        self.image = pygame.image.load("Assets/lobster.png") # load sprite image
        self.image = pygame.transform.scale(self.image, (self.size, self.size)) #resizes sprite image

    def move(self):
        self.check_walls()
        self.x += self.speedX
        self.y += self.speedY
    
    def check_walls(self):
        if self.x < 0 or self.x > SCREEN_WIDTH - self.size:
            self.x -= self.speedX
            self.speedX  = 0
        if self.y < 0 or self.y > SCREEN_HEIGHT - self.size:
            self.y -= self.speedY
            self.speedY  = 0
    
    def draw(self, screen):
        screen.blit(self.image, [self.x, self.y]) #draws sprite image




##### Colours #####
# sourcery skip: merge-comparisons
BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
RED   = (255,   0,   0)

##### Screen Initialisation #####
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720
size = (SCREEN_WIDTH, SCREEN_HEIGHT)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Lobster Game")

#Background loading and transforming
background = pygame.image.load("assets/sand.jpg") #Load the background
background = pygame.transform.scale(background, (SCREEN_WIDTH, SCREEN_HEIGHT)) #scales background to screen size

lob  = lobster() #makes lob equal to the class lobster
done = False              #Prepares the quit variable
clock = pygame.time.Clock() #prepares the clock variable

##### Main Program Loop #####
while not done:
    ##### Events Loop #####
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN: #TODO: Put this in a separate function within the class lobster
            if event.key == pygame.K_LEFT:
                lob.speedX = -3
            elif event.key == pygame.K_RIGHT:
                lob.speedX = 3
            if event.key == pygame.K_UP:
                lob.speedY = -3
            elif event.key == pygame.K_DOWN:
                lob.speedY = 3
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                lob.speedX = 0
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                lob.speedY = 0

    #Movement 
    lob.move()
    
    #drawing
    screen.fill(BLACK)
    screen.blit(background, (0,0))
    lob.draw(screen)
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
