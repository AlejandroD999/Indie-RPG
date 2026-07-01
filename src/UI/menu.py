from ..config import SCREEN_WIDTH, SCREEN_HEIGHT
from ..paths import MAIN_MENU_STATICS
import pygame
import os

class MainMenu():
    def __init__(self, app):
        self.app = app
        self.menu_buttons = {}
        self.possible_buttons = ["play", "options", "quit"] 

        
        self.raw_bg = pygame.image.load(
            os.path.join(MAIN_MENU_STATICS, "green_art.png")
        )

        self.background_image = pygame.transform.scale(self.raw_bg, self.app.screen_size) 
        self.init_elements()
        
    def init_elements(self):

        for button_type in self.possible_buttons:
            button_image =  pygame.image.load(os.path.join(MAIN_MENU_STATICS, f"{button_type}_button.png"))

            self.menu_buttons[button_type] = {
                "image": button_image,
                "rect": button_image.get_rect()
            }

    def mouse_collision(self, mouse_pos, object):
        return object.collidepoint(mouse_pos)

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()

                if self.mouse_collision(mouse_pos, self.play_rect):
                    self.app.change_screen(self.app.game)
                    return
    def update(self):
        pass

    def draw(self):
        self.app.screen.blit(self.background_image, (0, 0))
        btns_y_pos = []
        for button_type in self.possible_buttons:
            btn_img = self.menu_buttons[button_type]["image"]
            btn_rect = self.menu_buttons[button_type]["rect"]

            self.app.screen.blit(btn_img, (100, 100))


        pygame.display.flip()
