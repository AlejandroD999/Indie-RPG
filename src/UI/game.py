from ..sprites.player import Player
from ..sprites.enemy import Enemy
from .health_bar import HealthBar
from ..paths import BG_IMAGE_PATH
import pygame
import sys

class Game:
    def __init__(self, app):
        self.app = app
        pygame.display.set_caption("Ethereal RPG")
         
        self.player = Player(self.app.camera, self.app.camera.ground_rect.width / 2, (self.app.screen_size[1] - (self.app.screen_size[1] / 4))) 
        self.enemy = Enemy(self.player, 
                           self.app.camera.ground_rect.width / 2, (self.app.screen_size[1] - (self.app.screen_size[1] / 4)),
                           size = (self.app.screen_size[0] // 12, self.app.screen_size[1] // 6)
                           )

        self.app.camera.add(self.enemy)
        self.app.camera.add(self.player)
        
        self.health_bar = HealthBar(self.app.screen, 5, 5, 250, 25, self.player.hp) 

    def end_game(self):
        self.player.kill()

        self.app.change_screen(self.app.main_menu)        

    def update(self):
        self.player.update()
        self.enemy.update()
        self.health_bar.update(self.player.hp)

    def handle_events(self):
        ''' Handle all game events'''

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.app.running = False

            self.player.handle_event(event)            
    
    def draw(self):
        self.app.camera.custom_draw(self.player)
        self.health_bar.draw()
        pygame.display.flip()
