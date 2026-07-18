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
        self.define_health_bars() 
        
        self.app.camera.add(self.enemy)
        self.app.camera.add(self.player)

        
    
    def define_health_bars(self):
        self.player_health_bar = HealthBar(self.app.screen, 5, 5, 250, 25, self.player.hp) 

        self.enemy_health_bar = HealthBar(
                self.app.screen, 
                self.enemy.rect.x, self.enemy.rect.top * 1.25, 
                self.enemy.rect.width // 2, 
                self.enemy.rect.height // 10, 
                self.enemy.hp,
                self.enemy
                )

    def end_game(self):
        self.player.kill()

        self.app.change_screen(self.app.main_menu)        

    def update(self):
        self.player.update()
        self.player_health_bar.update(self.player.hp)
        
        self.enemy.update()
        self.enemy_health_bar.update(self.enemy.hp)

    def handle_events(self):
        ''' Handle all game events'''

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.app.running = False

            self.player.handle_event(event)            
    
    def draw(self):
        self.app.camera.custom_draw(self.player)

        self.player_health_bar.draw()
        self.enemy_health_bar.draw(self.app.camera)
        pygame.display.flip()
