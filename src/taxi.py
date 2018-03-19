import pygame

# WINDOW SIZE
WIDTH = 800
HEIGHT = 600

# COLORS
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

# STRINGS
NAME = "Scratch"

# INITIALIZE PYGAME
pygame.init() #initializes pygame
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption(NAME)

x = 50 #x starting chord for player
y = 50 #y starting chord for player
width = 40 # we'll use this for our player for now
height = 40 # ^
velocity = 5 #velocity
z = 450 #x chord for target
q = 450 #y chord for target

#main loop
run = True
while run:
    pygame.time.delay(100) #100 milliseconds
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT: #if you hit the red X to close the porgram, it will stop the loop
            run = False
    
    keys = pygame.key.get_pressed()
    #border detection
    if keys[pygame.K_LEFT] and x > velocity:
        x -= velocity
    if keys[pygame.K_RIGHT] and x < WIDTH - width:
        x += velocity
    if keys[pygame.K_UP] and y > velocity:
        y -= velocity
    if keys[pygame.K_DOWN] and y < HEIGHT - height:
        y += velocity

    win.fill((0, 0, 0))
    player = pygame.draw.rect(win, (RED), (x, y, width, height))
    player #drawing our player proto
    target = pygame.draw.rect(win, (YELLOW), (z, q, width, height))
    target #drawing our target proto, the place we want to bring our player to
    if player == target: #if they are the same position (...) will happen
        win.fill((YELLOW)) #placeholder, can add some relevant function later, for now the screen will turn yellow
    pygame.display.update()

pygame.quit() 
