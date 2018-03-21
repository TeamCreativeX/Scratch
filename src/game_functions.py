import sys
from time import sleep

import pygame

def check_events(screen, stats, sb, play_button, ship, aliens, bullets):
    ''' Respond to kepresses and mouse events '''
    # Watch for keyboard and mouse events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_button_clicked(mouse_x, mouse_y)