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
        pygame.draw.rect(screen, WHITE, [lob.x, lob.y, lob.size, lob.size])

##### Colours #####
BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
RED   = (255,   0,   0)

##### Screen Initialisation #####
SCREEN_WIDTH = 700
SCREEN_HEIGHT = 500
size = (SCREEN_WIDTH, SCREEN_HEIGHT)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Lobster Game")

lob  = lobster()
done = False              
clock = pygame.time.Clock()

##### Main Program Loop #####
while not done:
    ##### Events Loop #####
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN:
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

    #Movement and drawing
    lob.move()
    
    screen.fill(BLACK)
    lob.draw(screen)
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
