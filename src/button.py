
import pygame.font

class Button():
    '''
    Button class to create individual buttons
    '''

    def __init__(self, screen, x_cord, y_cord, height, message):
        ''' Initialize button attributes '''
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.message = message

        # Set the dimensions and properties of the button
        self.width = 250
        self.height = height
        self.x_cord = x_cord
        self.y_cord = y_cord
        self.button_color = (0, 255, 191)
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 48)

        # Build the button's rect object and center it
        self.rect = pygame.draw.rect(self.screen, self.button_color, (x_cord, y_cord, self.width, self.height), 0)

        # The button message needs to be prepped only once
        self.prep_msg(message)

    def prep_msg(self, message):
        ''' Turn msg into a rendered image and center text on the button '''
        self.msg_image = self.font.render(self.message, True, self.text_color, self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

        self.draw_button()

    def draw_button(self):
        # Draw blank button and then draw image
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)