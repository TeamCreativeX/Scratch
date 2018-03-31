import math
import pygame
from file_manipulation import load_image
from constant import *

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
        self.original_image = load_image('player.png')
        self.original_image.set_colorkey(self.original_image.get_at((0,0)))
        self.image = self.original_image
        self.test = False
        self.rect = self.image.get_rect()

        self.crashed = False # Temporary loose condition


        # Speed related value in pixel
        self.speed = 0 # Initial speed is 0, car is stopped.
        self.acceleration = 0.40 # Arbitrary value
        self.max_speed = 10 # Arbitrary value

        # Backward speed related value in pixel
        self.backward_acceleration = 0.30
        self.backward_max_speed = 4

        # Break related value in pixel
        self.deceleration = 0.35 # Arbitrary value
        self.natural_deceleration = 0.15

        # Direction of the car in degrees, counterclockwise
        self.direction = 0

        # Turning related value in degrees
        self.turn_speed = 0
        self.turn_acceleration = 0.1
        self.max_turn = 6
        self.min_turn = -6

        #locgic boolean
        self.is_moving = False

    def rotate_image(self, angle):
        "Rotate the image around the center"
        self.image = rot_image = pygame.transform.rotate(self.original_image, angle)
        self.rect = rot_image.get_rect(center=self.rect.center)

    def update(self,keystate):
        """ Override the default routine
        The update method is called on each cycle and should contain
        the main logic about updating the status of the car object
        /!\ This method is a work in progress, still lot of logic missing
        """

        # This logic is still elementary and should be splitted in different methods

        #logic if car is moving
        if self.speed > 0 or self.speed < 0:
            self.is_moving = True
        else:
            self.is_moving = False

        #chaning the turn speed when speed is slow [need more improvement]
        if self.speed < 5 and self.speed > -4:
            if self.turn_speed < 0:
                self.turn_speed = -2
            else:
                self.turn_speed = 2
        elif self.speed < 3 and self.speed > -2:
            if self.turn_speed < 0:
                self.turn_speed = -0.5
            else:
                self.turn_speed = 0.5

        #resetting  the truning speed when stationary
        if not self.is_moving:
            self.turn_speed = 0


        # Acceleration
        if keystate[pygame.K_UP] and self.speed <= self.max_speed:
            self.speed = self.speed + self.acceleration

        # Backward acceleration
        if keystate[pygame.K_DOWN] and self.speed <= 0 and self.speed * -1 < self.backward_max_speed:
            self.speed = self.speed - self.backward_acceleration

        # Deceleration
        if keystate[pygame.K_DOWN] and self.speed > 0:
            self.speed = self.speed - self.deceleration

        # Natural break
        if not keystate[pygame.K_DOWN] and not keystate[pygame.K_UP]:
            if self.speed >= 0.15:
                self.speed = self.speed - self.natural_deceleration
            elif self.speed <= -0.15:
                self.speed = self.speed + self.natural_deceleration
            else:
                self.speed = 0

        # Turning left and right, should work with one method
        # Turn left
        if keystate[pygame.K_LEFT] and self.is_moving:
            # Reset turn speed if turning in other direction
            if self.turn_speed < 0:
                self.turn_speed = 0
            if self.turn_speed <= self.max_turn:
                self.turn_speed = self.turn_speed + self.turn_acceleration


        # Turn right
        if keystate[pygame.K_RIGHT] and self.is_moving:
            if self.turn_speed > 0:
                self.turn_speed = 0
            if self.turn_speed >= self.min_turn:
                self.turn_speed = self.turn_speed - self.turn_acceleration



        # Reset turn speed
        if not keystate[pygame.K_RIGHT] and not keystate[pygame.K_LEFT]:
                self.turn_speed = 0

        # Update direction
        if self.is_moving:
            self.direction = self.direction + self.turn_speed
        # Update image direction
        self.rotate_image(self.direction)

        # Update care position, read about trigonotry.
        self.rect = self.rect.move(math.sin(math.radians(self.direction)) * \
            self.speed, math.cos(math.radians(self.direction)) * self.speed)
