import time

import pygame
import random
import sys

pygame.init()
w = 500
h = 500
screen = pygame.display.set_mode((w,h))
font = pygame.font.SysFont(None,20)
font2 = pygame.font.SysFont(None,30)
font3 = pygame.font.SysFont(None,30)
font4 = pygame.font.SysFont(None,30)
font5 = pygame.font.SysFont(None,30)

key = pygame.key.get_pressed()
fps = pygame.time.Clock()
bg = pygame.image.load('snakebg.jpg')
snake = [[200, 200], [200, 200], [200, 200], [200, 200]]
s_position = [200, 200]
food = [random.randrange(1, (w // 10)) * 10, random.randrange(1, (w // 10)) * 10]
spawn = True
move = 'r'
change = move
score = 0
run = True


def start():
    global snake,s_position,food,spawn,run,move,change,score
    snake = [[200, 200], [200, 200], [200, 200], [200, 200]]
    s_position = [200, 200]
    food = [random.randrange(1, (w // 10)) * 10, random.randrange(1, (w // 10)) * 10]
    spawn = True
    move = 'r'
    change = move
    score = 0
    run = True



def scoree():
    global score
    score_f = font.render('nigga ya score: '+str(score),True,'red')
    screen.blit(score_f,(50,50))

def foods():
    global snake
    global s_position
    global food
    global spawn
    global score
    if s_position == food:
        spawn = False
        score += 1
    else:
        snake.pop()
    if not spawn:
        food = [random.randrange(1, (w // 10)) * 10, random.randrange(1, (w // 10)) * 10]
def movee(first,second):
    global move
    global change
    if change == first and move != second:
        move = first
def runn():
    global s_position
    global move
    if move == 'u':
        s_position[1] -= 10
    if move == 'd':
        s_position[1] += 10
    if move == 'r':
        s_position[0] += 10
    if move == 'l':
        s_position[0] -= 10
    snake.insert(0, list(s_position))
def firstrun():
    global change
    if event.key == pygame.K_UP:
        change = "u"
    if event.key == pygame.K_DOWN:
        change = "d"
    if event.key == pygame.K_RIGHT:
        change = "r"
    if event.key == pygame.K_LEFT:
        change = "l"
def secondrun():
    if change == 'u':
        movee('u', 'd')
    elif change == 'd':
        movee('d', 'u')
    elif change == 'r':
        movee('r', 'l')
    elif change == 'l':
        movee('l', 'r')
def gameover():
    global key
    screen.fill('black')
    gemover = font2.render("GAMEOVER",True,'red')
    again = font3.render("press R to restart",True,'red')
    ded = font5.render("press Q to quit",True,'red')
    urscore = font4.render("SCORE = "+str(score),True,'red')
    screen.blit(again,(100,80))
    screen.blit(urscore,(100,140))
    screen.blit(gemover,(100,200))
    screen.blit(ded,(100,20))
    pygame.display.flip()
    wait = True
    while wait:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    quit()
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_r:
                    wait = False
                    start()


while run:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif event.type == pygame.KEYDOWN:
            firstrun()
            secondrun()
    screen.fill('white')
    scoree()

    for i in snake:
        pygame.draw.rect(screen, 'red', pygame.Rect(i[0], i[1], 10, 10))
    pygame.draw.rect(screen, 'green', pygame.Rect(food[0], food[1], 10, 10))
    runn()
    foods()
    spawn = True
    if s_position[0] > w:
        s_position[0] = 0
    if s_position[0] < 0:
        s_position[0] = 390
    if s_position[1] > h:
        s_position[1] = 0
    if s_position[1] < 0:
        s_position[1] = 390
    for block in snake[1:]:
        if block == s_position:
            gameover()
    pygame.display.update()
    fps.tick(10)
pygame.quit()
sys.exit()
