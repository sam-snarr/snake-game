import pygame
from pygame.locals import *
import sys 
import random

pygame.init()

x_width = 720
y_width = 480
screen = pygame.display.set_mode((x_width, y_width))

def gameover():
    '''displays message when game is over and then waits for keypress to exit'''
    font = pygame.font.Font('freesansbold.ttf',35)
    textSurface = font.render('Game over: Press key to quit', True, (0,0,0))
    textRect = textSurface.get_rect()
    textRect.center = (x_width/2, y_width/2)
    screen.blit(textSurface, textRect) 
    pygame.display.update()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN or event.type == pygame.MOUSEBUTTONDOWN or event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

def show_score():
    '''displays score in top left part of screen'''
    font = pygame.font.Font('freesansbold.ttf',20)
    textSurface = font.render('score: {}'.format(score), True, (0,0,0))
    textRect = textSurface.get_rect()
    textRect.left = 10
    textRect.top = 10

    screen.blit(textSurface, textRect) 
    pygame.display.update()


# creates snake
snake_array = []
for i in range(3):
    r = pygame.Rect(100-i*10, 100, 10, 10)
    snake_array.append(r)

# create fruit
fruit = pygame.Rect(random.randint(0, x_width/10)*10, random.randint(0, y_width/10)*10, 10, 10   )
dir='RIGHT'
score=0

# main loop 
while True:
    # set framerate (higher is more difficult)
    pygame.time.Clock().tick(10) 

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:   
            #checks what key is pressed and makes sure that it is not in the reverse direction that snake is currently moving
            if event.key == pygame.K_UP and dir != 'DOWN':
                dir = 'UP'
            elif event.key == pygame.K_RIGHT and dir != 'LEFT':
                dir = 'RIGHT'
            elif event.key == pygame.K_LEFT and dir != 'RIGHT':
                dir = 'LEFT'
            elif event.key == pygame.K_DOWN and dir != 'UP':
                dir = 'DOWN'

    # get head of snake
    head = snake_array[0]
    head_x = head.x
    head_y = head.y

    # depending what direction is pressed, insert a new head in that direction
    if dir=='UP':
        snake_array.insert(0, pygame.Rect(head_x, head_y-10, 10,10))
    elif dir=='RIGHT':
        snake_array.insert(0, pygame.Rect(head_x+10, head_y, 10,10))
    elif dir=='LEFT':
        snake_array.insert(0, pygame.Rect(head_x-10, head_y, 10,10))
    elif dir=='DOWN':
        snake_array.insert(0, pygame.Rect(head_x, head_y+10, 10,10))

    # if snake touches fruit then it grows one unit by keeping its tail between frames, otherwise it loses one unit
    if snake_array[0].x == fruit.x and snake_array[0].y == fruit.y:
        score += 1
        fruit.x = random.randint(0, x_width/10)*10
        fruit.y = random.randint(0, y_width/10)*10
    else:
        snake_array.pop()
    
    # checks if snake goes outside of box
    if snake_array[0].x < 0 or snake_array[0].x > x_width or snake_array[0].y < 0 or snake_array[0].y > y_width:
        gameover()

    # checks if snake touches itself
    for r in snake_array[1:]:
        if snake_array[0].x == r.x and snake_array[0].y == r.y:
            gameover()

    # fill screen with color to remove prior pieces
    screen.fill((60,15,200, 1))

    # draw each rectangle of snake
    for r in snake_array:
        pygame.draw.rect(screen, (255,255,255), r, 1)
    
    show_score()

    # draw the fruit
    pygame.draw.rect(screen, (0, 255, 0), fruit, 0)

    
    pygame.display.update()
            
        
            
        
    