from ..config import SCREEN_WIDTH, SCREEN_HEIGHT
from ..paths import MAIN_MENU_STATICS
from .elements import Button
import pygame
import os

class MainMenu():
    def __init__(self, app):
        self.app = app
        self.screen_width = self.app.screen_size[0]
        self.screen_height = self.app.screen_size[1]
        self.menu_buttons = {}
        self.possible_buttons = ["play", "options", "quit"] 

        
        self.raw_bg = pygame.image.load(
            os.path.join(MAIN_MENU_STATICS, "green_art.png")
        )

        self.background_image = pygame.transform.scale(self.raw_bg, self.app.screen_size) 
        self.init_elements()
        
    def init_elements(self):
        btn_x = self.screen_width / 2
        btn_y = self.screen_height / 4 

        for button_type in self.possible_buttons:
            raw_btn_img =  pygame.image.load(os.path.join(MAIN_MENU_STATICS, f"{button_type}_button.png")).convert_alpha()
            
            btn_img = pygame.transform.scale(raw_btn_img, (self.screen_width / 4, self.screen_height / 6))
            btn_x = self.screen_width // 2 - (btn_img.get_width() / 2)
            btn_margin = btn_img.get_height() + (btn_img.get_height() / 8)

            self.menu_buttons[button_type] = Button(btn_img, btn_x, btn_y)                
            btn_y += btn_margin

            

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
        for button_type in self.possible_buttons:
            btn = self.menu_buttons[button_type]
            
            # btn_img = self.menu_buttons[button_type]["image"]
            # btn_rect = self.menu_buttons[button_type]["rect"]

            self.app.screen.blit(btn.get_img(), btn.get_pos())


        pygame.display.flip()
