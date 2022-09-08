# Nikolai and contributors
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
        self.rectvalue = pygame.Rect(self.x, self.y, self.size, self.size)

    def move(self):
        self.check_walls()
        self.x += self.speedX
        self.y += self.speedY
        self.rectvalue = pygame.Rect(self.x, self.y, self.size, self.size)
    
    def check_walls(self):
        if self.x < 0 or self.x > SCREEN_WIDTH - self.size:
            self.x -= self.speedX
            self.speedX  = 0
        if self.y < 0 or self.y > SCREEN_HEIGHT - self.size:
            self.y -= self.speedY
            self.speedY  = 0
    
    def draw(self, screen):
        screen.blit(self.image, [self.x, self.y]) #draws sprite image

class worm(): #Creates a worm class that will be eaten by the player
    def __init__(self):
        self.size = 30
        self.x = random.randrange(0, SCREEN_WIDTH-self.size)
        self.y = random.randrange(0, SCREEN_HEIGHT-self.size)
        self.eaten = False
        self.rectvalue = pygame.Rect(self.x, self.y, self.size, self.size)
        self.image = pygame.image.load("Assets/worm.png")
        self.image = pygame.transform.scale(self.image, (self.size, self.size))
    def collisionCheck(self, lobsterRect):
        global score
        self.eaten = self.rectvalue.colliderect(lobsterRect)
        if self.eaten == True: 
            self.x = random.randrange(0, SCREEN_WIDTH-self.size)
            self.y = random.randrange(0, SCREEN_HEIGHT-self.size) 
            self.rectvalue = pygame.Rect(self.x, self.y, self.size, self.size)
            score += 1
            eat.play()
    def draw(self):
        screen.blit(self.image, (self.x, self.y))
    


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
pygame.display.set_caption("Lobster Game, By Tap")

##### Loading #####
#Background loading and transforming
background = pygame.image.load("assets/sand.jpg") #Load the background
background = pygame.transform.scale(background, (SCREEN_WIDTH, SCREEN_HEIGHT)) #scales background to screen size

#Load Sounds
eat = pygame.mixer.Sound("assets/bite.mp3")

#Load Font
myfont = pygame.font.Font(None, 75) #Load the default font

##### Variables #####
lob  = lobster() #makes lob equal to the class lobster
wom = [worm() for i in range(100)] #makes wom equal to the class worm

global score
time = 60*60 #seconds times fps
score = 0

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
    for worm in wom:
        worm.collisionCheck(lob.rectvalue)
    time -= 1
    
    #drawing
    screen.fill(BLACK)
    screen.blit(background, (0,0))
    for worm in wom:
        worm.draw()
    lob.draw(screen)
    screen.blit(myfont.render("Score: "+str(score), True, BLACK), (0,0))
    screen.blit(myfont.render("Time: "+str(round(time/60, 1)), True, BLACK), (500,0))
    pygame.display.flip()
    clock.tick(60)

pygame.quit()