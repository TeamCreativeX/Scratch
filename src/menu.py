import pygame

class Menu:
    '''
    Menu class to add specified number of buttons to the game's home screen
    '''

    def __init__(self, screen):
        self.game_active = False
        self.screen = screen
        self.button_color = (0, 255, 191)
        self.text_color = (0, 0, 0)
        self.font = pygame.font.SysFont(None, 48)
        self.width = 250
        self.num_buttons = 4
        self.button_messages = ['Play', 'Temp', 'Temp', 'Temp']
        self.buttons = []

        self.prep_buttons(self.screen)

    def draw_button(self, x_cord, y_cord, button_height, message):
        # Create buttons and append to buttons list
        button = pygame.draw.rect(self.screen, self.button_color, (x_cord, y_cord, self.width, button_height), 0)
        self.msg_image = self.font.render(message, True, self.text_color, self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = button.center
        self.screen.blit(self.msg_image, self.msg_image_rect)

    def prep_buttons(self, screen):
        # Draw buttons on the screen
        screen_rect = screen.get_rect()
        screen_height = screen_rect.height
        screen_centery = screen_rect.centery
        button_height = screen_height // ((self.num_buttons * 2) + 1)
        start_position = button_height

        for i in range(self.num_buttons):
            message = self.button_messages[i]
            self.draw_button(screen_centery, start_position, button_height, message)
            start_position += button_height * 2

    def check_button_clicked(self, mouse_x, mouse_y):
        # Check if a button was clicked
        pass
