#developed using Python 2.x
#Huzaifa Nasir

import pygame, sys, random, time
from pygame import gfxdraw
from pygame.locals import *


#global constants 
area = SCREEN_WIDTH, SCREEN_HEIGHT = 800,600
HEIGHT = 10
WIDTH = 10
BLACK = (0,0,0)
WHITE = (255,255,255)
GREEN = (0,255,0)
BLUE = (0,0,255)
DBLUE = (0,0,122)

#initializing the window
pygame.init()

screen = pygame.display.set_mode(area)
pygame.display.set_caption("Snake")



clock = pygame.time.Clock()


#scoreboard(score): display the current score of the user (10 points per fruit)
def scoreboard(score):
    font = pygame.font.Font("freesansbold.ttf", 20)
    text = font.render("Score: " + str(score), True, WHITE)
    screen.blit(text,(0,0))

#text_objects(text,font): draws the text on a new surface. Also gives the dimensions of the rectangle encasing the text
def text_objects(text, font):
    textSurface = font.render(text, True, WHITE)
    return textSurface, textSurface.get_rect()


#message_display(text): assigns the text a set font and font size, and moves it to the middle of the screen
def message_display(text):
    largeText = pygame.font.Font("freesansbold.ttf", 115)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = (SCREEN_WIDTH * 0.5, SCREEN_HEIGHT * 0.5)
    screen.blit(TextSurf, TextRect)
    
    pygame.display.update()
    time.sleep(2)
    game() 

#crash(): Lets the user know they have crashed using the message_display function
def crash():
    message_display("GAME OVER")


#drawing the fruit
def fruit(x, y, width, height, colour):
    pygame.draw.rect(screen, colour, [x,y,width,height])
    

#s_head(x,y): shifts the snake head x pixels right and y pixels down
def s_head(x,y):
    pygame.draw.rect(screen, GREEN, [x,y,WIDTH,HEIGHT])





def game():

    x = SCREEN_WIDTH * 0.45
    y = SCREEN_HEIGHT * 0.5
    snakeBlocks = []

    x_change = 0
    y_change = 0
    speed = 2

   # s_head = snake(screen, x,y)
    
    fruit_x = random.randrange(0,SCREEN_WIDTH-WIDTH)
    fruit_y = random.randrange(0, SCREEN_HEIGHT-HEIGHT)
    curScore = 0
    snakeBlocks = [(x,y), (x+10, y+10)]
    

#game loop
    start = True
    while start:
        for event in pygame.event.get():
            #quit the game
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        #the direction the user wants the snake to go in
        #when moving horizontally, y_change = 0 so the head doesn't move diagonally to avoid making the
        #game too complicated. Same thing when moving vertically
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -speed
                    y_change = 0
                elif event.key == pygame.K_RIGHT:
                    x_change = speed
                    y_change = 0
                elif event.key == pygame.K_UP:
                    y_change = -speed
                    x_change = 0 
                elif event.key == pygame.K_DOWN:
                    y_change = speed
                    x_change = 0
        x += x_change
        y += y_change
        screen.fill(BLACK)
        # creating fruit
        fruit(fruit_x, fruit_y, WIDTH, HEIGHT, BLUE)
        
        # changing location of snake head
        for (x,y) in snakeBlocks:
            s_head(x,y)

            
      # s_head(screen,x,y)
        scoreboard(curScore)

        new = pygame.draw.rect(screen,WHITE,[SCREEN_WIDTH+10, SCREEN_HEIGHT + 10, WIDTH, HEIGHT])
        #making the window "boundary-less"
        if x < 0 or x > SCREEN_WIDTH:
            x = SCREEN_WIDTH - x
        if y < 0 or y > SCREEN_HEIGHT:
            y = SCREEN_HEIGHT - y

        #eating the fruit
        if x >= fruit_x and x <= fruit_x + WIDTH or x + WIDTH >= fruit_x and x + WIDTH <= fruit_x + WIDTH:
            if y >= fruit_y and y <= fruit_y + HEIGHT or y +HEIGHT >= fruit_y and y + HEIGHT<= fruit_y + HEIGHT:
                fruit_y = random.randrange(0,SCREEN_HEIGHT-HEIGHT)
                fruit_x = random.randrange(0, SCREEN_WIDTH-WIDTH)
                curScore+=10
                speed+= 0.2
                
                
                
        
        pygame.display.update()
        clock.tick(60)

game()
pygame.quit()
quit()
