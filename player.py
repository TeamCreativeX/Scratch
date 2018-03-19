import pygame

#Develop on this class to make much more better movements for the player

class Player:
	#constant variables
	MAX_SPEED = 20 #max speed the player can move
	MAX_ACCELERATION = 10 #max acceleratrion of the player/car
	player_velocity = 0 #initial velocity of the player

	def __init__(self,x,y): #Constructor to initialize the player  class with the player cordinate
		self.x = x #x position of player
		self.y = y #y position of the player

	def add_force(self, force): #Add force to the player to simulate realistic movement
		self.add_acceleration(force) #adds the acceleration


	def add_acceleration(self, acceleration): #Add acceleartion to the player
		self.velocity(acceleartion)

	def velocity(self,speed):
		pass
		#need to think how its gonna work

