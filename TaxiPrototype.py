import pygame
pygame.init() #initializes pygame

win = pygame.display.set_mode((500, 500))
# coordinates are 0,0 on top left with pygame
pygame.display.set_caption("First Game")

screenwidth = 500

red = (255, 0, 0) #pygame uses RGB code for color
yellow = (255, 255, 0, 1) 
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
    if keys[pygame.K_RIGHT] and x < screenwidth - width:
        x += velocity
    if keys[pygame.K_UP] and y > velocity:
        y -= velocity
    if keys[pygame.K_DOWN] and y < screenwidth - height:
        y += velocity

    win.fill((0, 0, 0))
    player = pygame.draw.rect(win, (red), (x, y, width, height))
    player #drawing our player proto
    target = pygame.draw.rect(win, (yellow), (z, q, width, height))
    target #drawing our target proto, the place we want to bring our player to
    if player == target: #if they are the same position (...) will happen
        win.fill((yellow)) #placeholder, can add some relevant function later, for now the screen will turn yellow
    pygame.display.update()
    
pygame.draw.rect
pygame.quit()

    
