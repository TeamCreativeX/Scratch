# Extend sys path to utility folder, not sure about good practice, need advice on that
import sys
sys.path.insert(0, './utility/')

import os
import pygame
import core
import camera
from menu import Menu
from game_functions import check_events
from vehicle import Vehicle
from constant import *
from file_manipulation import load_image

def main():
    # INITIALIZE PYGAME pygame.SRCALPHA
    pygame.init()
    pygame.display.set_caption(TITLE)
    game_window = pygame.display.set_mode(SIZE)
    #game_background = pygame.Surface((2000,1000),pygame.SRCALPHA)

    # INITIALIZE CLOCK
    clock = pygame.time.Clock() # Initialize clock for later use

    # INITIALIZE GROUPS
    all = pygame.sprite.RenderUpdates()

    # INITIALIZE DEFAULT GROUPS TO EACH SPRITE CLASS
    Vehicle.containers = all

    # Create Menu
    menu = Menu(game_window)

    #test map
    map = load_image("test_map.png")

    car = Vehicle() # Create our player car object

    while RUNNING:
        check_events(menu)
        if menu.game_active:
            # Dirty fix to clear menu it should be cleared when game start not at every loop
            game_window.fill(WHITE) #
            game_window.blit(map,(-400,0))
            for event in pygame.event.get():
                if event.type == pygame.QUIT or \
                    (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                        return

            keystate = pygame.key.get_pressed() # Dict of key status

            #all.clear(game_window, game_background) # Clear the last drawn ssprite
            all.update(keystate) # Trigger update() hook on every sprite
            # DRAW SPRITE
            dirty = all.draw(game_window)

        pygame.display.update()
        clock.tick(30) # Cap FPS to 30 until delta time implementation

    pygame.quit()

# START THE GAME
if __name__ == '__main__':
    main()
