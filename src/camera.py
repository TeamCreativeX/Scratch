import pygame
class Camera:
    def __init__(self,width, height):
        self.camera = pygame.Rect(0,0,width,height)
        self.width = width
        self.height = height

    def render(self, entity):
        return entity.rect.move(self.camera.topleft)

    def update(self, player):
        x = -player.rect.x + int(self.width/2)
        y = -player.rect.y + int(self.height/2)
        self.camera = pygame.Rect(x,y,self.width, self.height)
