import pygame
pygame.init() #initialize pygame, always

win = pygame.display.set_mode((500, 500))
# coordinates top left
pygame.display.set_caption("First Game")

screenwidth = 500

red = (255, 0, 0)
yellow = (255, 255, 0, 1) 
x = 50 #x starting chord for player
y = 50 #y starting chord for player
width = 40
height = 40
velocity = 5 #velocity
z = 450 #x chord for target
q = 450 #y chord for target

#main loop
run = True
while run:
    pygame.time.delay(100) #100 milliseconds
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    keys = pygame.key.get_pressed()
    
    if keys[pygame.K_LEFT] and x > velocity:
        x -= vel
    if keys[pygame.K_RIGHT] and x < screenwidth - width:
        x += vel
    if keys[pygame.K_UP] and y > velocity:
        y -= vel
    if keys[pygame.K_DOWN] and y < screenwidth - height:
        y += vel

    win.fill((0, 0, 0))
    player = pygame.draw.rect(win, (red), (x, y, width, height))
    player
    target = pygame.draw.rect(win, (yellow), (z, q, width, height))
    target
    if player == target:
        win.fill((yellow))
    pygame.display.update()
    
pygame.draw.rect
pygame.quit()

    