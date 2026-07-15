from .config import SCREEN_WIDTH, SCREEN_HEIGHT
from .UI.camera import Camera
from .UI.game import Game
from .UI.menu import MainMenu
import pygame
import sys

class App:
    def __init__(self):
        pygame.init()
        self.screen_size = (SCREEN_WIDTH, SCREEN_HEIGHT) 
        self.screen = pygame.display.set_mode(self.screen_size)        
        self.running = True
        self.clock = pygame.time.Clock()
        
        self.camera = Camera()
        self.game = Game(self)
        self.main_menu = MainMenu(self)

        self.current_screen = self.main_menu
    
    def change_screen(self, screen):
        self.current_screen = screen

    def run(self):
        while self.running:

            self.current_screen.handle_events()
            self.current_screen.update()
            self.current_screen.draw()

            self.clock.tick(60)
        pygame.quit()
        sys.exit()

