import os
import pygame

# INITIALIZE PROJECT PATH
MAIN_DIR = os.path.dirname(os.path.realpath(__file__))

def load_image(file):
    #"loads an image, prepares it for play"
    image_dir = os.path.join(MAIN_DIR,'assets/images',file)
    try:
        surface = pygame.image.load(image_dir)
    except pygame.error:
        raise SystemExit('Could not load image "%s" %s'%(file, pygame.get_error()))
    return surface.convert()

def load_sound(sound_file):
    #path to sound file
    sound_dir = os.path.join(MAIN_DIR,"assets/music",sound_file)
    return sound_dir
