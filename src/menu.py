import pygame

class Menu:
    '''
    Menu class to add specified number of buttons to the game's home screen
    '''

    def __init__(self, screen):
        self.game_active
        self.screen = screen
        self.num_buttons = 4
        self.buttons = []

        for event in pygame.event.get()
             if event.type == pygame.QUIT:
                sys.exit()

            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                check_button_clicked(self, mouse_x, mouse_y)

    def create_button(height, width):
        # Create buttons and append to buttons list

    def draw_buttons(self, button, screen):
        # Draw buttons on the screen

    def check_button_clicked(self, mouse_x, mouse_y):
        # Check if a button was clicked