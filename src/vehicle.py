import math
import pygame
from file_manipulation import load_image

class Vehicle(pygame.sprite.Sprite):
    """ Vehicle class
    The vehicle inherit from Sprite https://www.pygame.org/docs/ref/sprite.html
    """

    def __init__(self):
        # INITIALIZE THE PARENT CLASS
        pygame.sprite.Sprite.__init__(self, self.containers)

        # INITIALIZE IMAGE
        # Save the original image as reference as successive rotations
        # will alter the quality of the image otherwise.
        self.original_image = load_image('vehicle_taxi.png')
        self.image = self.original_image

        self.rect = self.image.get_rect()

        self.crashed = False # Temporary loose condition

        self.direction = 0 # Direction of the car in degrees, counterclockwise

        # Speed related value are in pixel
        self.speed = 0 # Initial speed is 0, car is stopped.
        self.acceleration = 0.25 # Arbitrary value
        self.max_speed = 20 # Arbitrary value

        # Break speed relative value are in degrees
        self.break_speed = 0 # Initial break speed is 0
        self.break_acceleration = 0.25 # Arbitrary value
        self.max_break = 5

    def rotate_image(self, angle):
        "Rotate the image around the center"
        self.image = rot_image = pygame.transform.rotate(self.original_image, angle)
        self.rect = rot_image.get_rect(center=self.rect.center)

    def update(self, keystate):
        """ Override the default routine
        The update method is called on each cycle and should contain
        the main logic about updating the status of the car object
        /!\ This method is a work in progress, still lot of logic missing
        """
        if keystate[pygame.K_UP] and self.speed <= self.max_speed:
            self.speed = self.speed + self.acceleration
        elif keystate[pygame.K_DOWN]:
            self.speed = self.speed - 0.3
        elif self.speed > 0:
            self.speed = self.speed - 0.15
        if keystate[pygame.K_LEFT]: self.direction = self.direction + 2
        if keystate[pygame.K_RIGHT]: self.direction = self.direction - 2

        self.rotate_image(self.direction)
        self.rect = self.rect.move(math.sin(math.radians(self.direction)) * \
            self.speed, math.cos(math.radians(self.direction)) * self.speed)
