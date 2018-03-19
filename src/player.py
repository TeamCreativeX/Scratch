
import pygame

#Develop on this class to make much more better movements for the player
#my logic (You must be familiar with graphs to understand this) speed,velocity and force are a vector or array with values [X,Y] which has 3 state [0 = static doesnt move, 1 = in a positive direction for example if x is 1 ie positive it means right -1 negative direction]

class Player:
	#constant variables
	MAX_SPEED = 20 #max speed the player can move
	MAX_ACCELERATION = 10 #max acceleratrion of the player/car
	player_velocity = [0,0] #initial velocity of the player

	def __init__(self,x,y): #Constructor to initialize the player  class with the player cordinate
		self.x = x #x position of player
		self.y = y #y position of the player

	def add_force(self, force): #Add force to the player to simulate realistic movement
		self.add_acceleration(force) #adds the acceleration


	def add_acceleration(self, acceleration): #Add acceleartion to the player
		self.velocity(acceleartion) #Acceleration is a vector or array with thow values [X,Y] reppresent the direction of acceleration

	def velocity(self,speed):
		self.x = speed[0] #Speed is a vector or array with 2 values [X,Y] so speed[0] = X
		self.y = speed[1] #Y value of the speed

