# Extend sys path to utility folder, not sure about good practice, need advice on that
import sys
sys.path.insert(0, './utility/')

import os
import pygame
from vehicle import Vehicle

# WINDOW CONSTANT
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
WINDOW_NAME = "Scratch"

# COLORS
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

def main():
    # INITIALIZE PYGAME
    pygame.init()
    pygame.display.set_caption(WINDOW_NAME)
    game_window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    game_background = pygame.Surface((WINDOW_WIDTH, WINDOW_HEIGHT))

    # INITIALIZE CLOCK
    clock = pygame.time.Clock() # Initialize clock for later use

    # INITIALIZE GROUPS
    all = pygame.sprite.RenderUpdates()

    # INITIALIZE DEFAULT GROUPS TO EACH SPRITE CLASS
    Vehicle.containers = all

    car = Vehicle() # Create our player car object

    while car.crashed == False:
        for event in pygame.event.get():
            if event.type == pygame.QUIT or \
                (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                    return

        keystate = pygame.key.get_pressed() # Dict of key status

        all.clear(game_window, game_background) # Clear the last drawn ssprite
        all.update(keystate) # Trigger update() hook on every sprite

        # DRAW SPRITE
        dirty = all.draw(game_window)
        pygame.display.update(dirty)

        clock.tick(30) # Cap FPS to 30 until delta time implementation

    pygame.quit() 

# START THE GAME
if __name__ == '__main__':
    main()
