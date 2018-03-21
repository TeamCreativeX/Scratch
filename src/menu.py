import pygame

class Menu:
    '''
    Menu class to add specified number of buttons to the game's home screen
    '''

    def __init__(self, screen):
        self.game_active = False
        self.screen = screen
        self.button_color = (0, 255, 191)
        self.width = 250
        self.num_buttons = 4
        self.buttons = []

        self.prep_buttons(self.screen)

    def draw_button(self, x_cord, y_cord, button_height):
        # Create buttons and append to buttons list
        pygame.draw.rect(self.screen, self.button_color, (x_cord, y_cord, self.width, button_height), 0)

    def prep_buttons(self, screen):
        # Draw buttons on the screen
        screen_rect = screen.get_rect()
        screen_height = screen_rect.height
        screen_centery = screen_rect.centery
        button_height = screen_height // ((self.num_buttons * 2) + 1)
        start_position = button_height

        for i in range(self.num_buttons):
            self.draw_button(screen_centery, start_position, button_height)
            start_position += button_height * 2

    def check_button_clicked(self, mouse_x, mouse_y):
        # Check if a button was clicked
        pass
