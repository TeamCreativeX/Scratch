#music credits https://opengameart.org/content/the-gears-of-progress, https://opengameart.org/content/menu-music

import pygame
from file_manipulation import load_sound
class Sound:
    def __init__(self):
        pygame.mixer.init() #Initialize mixer


        #plays the music
    def playMusic(self):
        pygame.mixer.music.play(loops=-1)

        #stops the music
    def stopMusic(self):
        pygame.mixer.music.fadeout(1000)

        #loads the music
    def loadMusic(self,music):
        pygame.mixer.music.load(music)
