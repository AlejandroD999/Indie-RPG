from ..sprites.player import Player
from ..paths import BG_IMAGE_PATH, BUG_STATICS
import pygame
import sys

class Game:
    def __init__(self, app):
        self.app = app
        self.__bg_image = pygame.transform.scale(pygame.image.load(BG_IMAGE_PATH), self.app.screen_size).convert()
        pygame.display.set_caption("Ethereal RPG")
                
        self.player = Player(10, (self.app.screen_size[1] - (self.app.screen_size[1] / 4))) 
        
        self.app.camera.add(self.player)
        

    def update(self):
        self.player.update()

    def handle_events(self):
        ''' Handle all game events'''

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.app.running = False

            self.player.handle_event(event)            
    
    def draw(self):
        self.app.camera.custom_draw(self.player)
        pygame.display.flip()
