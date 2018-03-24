#This  will  be a core file of the game which will consit of usefull functions like intro, pause etc

import pygame
import sys
import time #time functions

class Game():
    def  __init__(self,gameWindow,run):
        self.gameWindow = gameWindow #gamw window reference
        self.run = run #main loop reference
        self.intro_image = [pygame.image.load("assets/intro.png"),pygame.image.load("assets/intro2.png")] #image assets
        self.pause_image = [] #pause image assets
        self.show_intro = True #intro loop
        self.target = 0 #target image
        self.pause_game = True #pause loop
        self.last = pygame.time.get_ticks() #time at which the Game class initialized

    def introAnimation(self): #function to lop through images at intro screen
        self.gameWindow.blit(self.intro_image[self.target],(0,0)) #draws image according to index
        if self.target == 0: #change the index
            self.target = 1
        else:
            self.target = 0




    def intro(self): #intro function shows intro
        while self.show_intro:
            self.now = pygame.time.get_ticks() #current time
            for event in pygame.event.get(): #get all the events
                if event.type == pygame.QUIT:
                    self.run = False #main loop boolean
                    self.show_intro = False #stop the intro loop
                    sys.exit()

                elif event.type == pygame.MOUSEBUTTONUP or event.type == pygame.MOUSEBUTTONDOWN: #if mouse pressed stop the intro
                    self.show_intro = False
            if self.now - self.last >= 700: #if its been .7 seconds
                self.introAnimation() #animate the intro screen
                self.last = self.now #last time is now current time
            pygame.display.flip() ##update the screen with intro image


    def pause(self): #pause the game whenever escape key is pressed
        while self.pause_game:
            for event in pygame.event.get(): #gets all the events
                if event.type == pygame.QUIT:
                    self.run = False
                    sys.exit()
                if event.type == pygame.KEYDOWN: #if key is being pressed
                    if event.key == pygame.K_ESCAPE: #if key is escape key
                        if self.pause_game == True:
                            self.pause_game = False #stop the loop

            self.gameWindow.blit(self.intro_image[0],(0,0)) #draw the pause scrren
            pygame.display.flip() #update the screen
