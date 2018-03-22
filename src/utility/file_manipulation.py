import os
import pygame

# INITIALIZE PROJECT PATH
MAIN_DIR = os.path.split(os.path.abspath(''))[0]

def load_image(file):
    "loads an image, prepares it for play"
    file = os.path.join(MAIN_DIR, 'src/assets', file)
    try:
        surface = pygame.image.load(file)
    except pygame.error:
        raise SystemExit('Could not load image "%s" %s'%(file, pygame.get_error()))
    return surface.convert()

