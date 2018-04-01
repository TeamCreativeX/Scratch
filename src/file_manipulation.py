#import os

import pygame
from pathlib import Path

# INITIALIZE PROJECT PATH
#MAIN_DIR = os.path.split(os.path.abspath(''))[0]
ASSETS = Path("assets/")

def load_image(file):
    "loads an image, prepares it for play"
    file = str(ASSETS / file)
    try:
        surface = pygame.image.load(file)
    except pygame.error:
        raise SystemExit('Could not load image "%s" %s'%(file, pygame.get_error()))
    return surface.convert()
