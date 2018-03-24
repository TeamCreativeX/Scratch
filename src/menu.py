import pygame

from button import Button

class Menu:
    '''
    Menu class to add specified number of buttons to the game's home screen
    '''

    def __init__(self, screen):
        ''' Initialize menu atttributes '''
        self.game_active = False
        self.screen = screen
        self.num_buttons = 4
        self.button_messages = ['Play', 'Temp', 'Temp', 'Temp']
        self.buttons = []

        self.prep_buttons(self.screen)

    def prep_buttons(self, screen):
        # Call button class to create individual buttons
        screen_rect = screen.get_rect()
        screen_height = screen_rect.height
        button_height = screen_height // ((self.num_buttons * 2) + 1)
        x_cord = screen_rect.centery
        y_cord = button_height

        for i in range(self.num_buttons):
            message = self.button_messages[i]
            button = Button(screen, x_cord, y_cord, button_height, message)
            self.buttons.append(button)
            y_cord += button_height * 2

    def check_button_clicked(self, mouse_x, mouse_y):
        # Check if a button was clicked
        for button in self.buttons:
            button_clicked = button.rect.collidepoint(mouse_x, mouse_y)

            if button_clicked and button.message == 'Play':
                self.game_active = True
