#This  will  be a core file of the game which will consit of usefull functions like intro, pause etc

import pygame
import time #time functions

intro_img = [pygame.image.load("assets/intro.png"),pygame.image.load("assets/intro2.png")] #image assets
target = 0 #target to show in image array
show_intro = True #introo loop

def intro(gameWindow):
    global show_intro,target

    while show_intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False #main loop boolean
                show_intro = False

            elif event.type == pygame.MOUSEBUTTONUP or event.type == pygame.MOUSEBUTTONDOWN: #if mouse pressed stop the intro
                show_intro = False

        gameWindow.blit(intro_img[target],(0,0)) #drawing the image
        pygame.display.flip() ##update the screen with intro image
        if target == 0: #changing the target image
            target = 1
        else:
            target = 0
        time.sleep(1) #1 secon delay for animaation IMORTANT TO DO:- NEED TO FIND ALTERNATIVE WAY TO CHANGE IMAGE AFTER 1 SEC WHITOUT STOPPING THE LOOP
