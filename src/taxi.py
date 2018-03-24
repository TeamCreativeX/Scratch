import pygame
import sys
import Core #importing core file which implements intro screen

# WINDOW SIZE
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600

# COLORS
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

# STRINGS
title = "Scratch"

# INITIALIZE PYGAME
pygame.init() #initializes pygame
game_window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption(title)
pause = False
x = 50 #x starting chord for player
y = 50 #y starting chord for player
width = 40 # we'll use this for our player for now
height = 40 # ^
velocity = 5 #velocity
z = 450 #x chord for target
q = 450 #y chord for target

#main loop
run = True
game = Core.Game(game_window,run)
while run:
    pygame.time.delay(100) #100 milliseconds
    #Core.intro(game_window) #shows the intro
    game.intro()


    for event in pygame.event.get():
        if event.type == pygame.QUIT: #if you hit the red X to close the porgram, it will stop the loop
            run = False
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                game.pauseGame = True
                game.pause()


    keys = pygame.key.get_pressed()
    #border detection
    if keys[pygame.K_LEFT] and x > velocity:
        x -= velocity
    if keys[pygame.K_RIGHT] and x < WINDOW_WIDTH - width:
        x += velocity
    if keys[pygame.K_UP] and y > velocity:
        y -= velocity
    if keys[pygame.K_DOWN] and y < WINDOW_HEIGHT - height:
        y += velocity

    game_window.fill((0, 0, 0))
    player = pygame.draw.rect(game_window, (RED), (x, y, width, height))
    player #drawing our player proto
    target = pygame.draw.rect(game_window, (YELLOW), (z, q, width, height))
    target #drawing our target proto, the place we want to bring our player to
    if player == target: #if they are the same position (...) will happen
        game_window.fill((YELLOW)) #placeholder, can add some relevant function later, for now the screen will turn yellow
    pygame.display.update()

pygame.quit()
